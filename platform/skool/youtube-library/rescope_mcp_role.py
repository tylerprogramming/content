#!/usr/bin/env python3
"""Re-scope the Attend MCP role mcp_tyler_attend to Tyler's current customer.

Runs provision.sql's grants + policies + proof via the Supabase Management API
(no admin DSN on the box). Skips provision.sql's role/password block on purpose:
the role exists and its password is in /root/attend/mcp/.env, so we keep it.
Also drops the stale `mcp_tyler_scope` policies that named a deleted customer.
usage: /opt/scripts/.venv/bin/python rescope_mcp_role.py [--apply]
"""
import os, re, sys, requests

ROLE = "mcp_tyler_attend"
CUSTOMER = "f769d47f-b4d4-4171-903a-e6a429ba3872"
REF = "fdhqdggjrkgqbtyeyrmw"
env = dict(l.strip().split("=", 1) for l in open("/root/.claude/skills/.env")
           if "=" in l and not l.lstrip().startswith("#"))
TOKEN = env["SUPABASE_ACCESS_TOKEN"].strip('"')

src = open("/root/attend/mcp/provision.sql").read()
body = src[src.index("grant usage on schema public"):src.index("-- Prove it.")]  # drop role/password block and
# the SET ROLE proof (Management API user can't SET ROLE); the proof is re-done below by logging in AS the role.
body = body.replace(":'role_name'", f"'{ROLE}'").replace(':"role_name"', f'"{ROLE}"')
body = body.replace(":'customer_id'", f"'{CUSTOMER}'")
assert ":'" not in body and ':"' not in body, "unrendered psql var left"

drop_old = "\n".join(
    f'drop policy if exists mcp_tyler_scope on public.{t};' for t in
    ["comment_campaign_responses", "comment_campaigns", "communities", "community_posts",
     "course_progress", "courses", "customers", "dm_messages", "dm_thread_state", "inbox",
     "member_insights", "members", "scheduled_posts"])
sql = "begin;\n" + drop_old + "\n" + body + "\ncommit;"

def q(s):
    r = requests.post(f"https://api.supabase.com/v1/projects/{REF}/database/query",
                      headers={"Authorization": f"Bearer {TOKEN}"}, json={"query": s}, timeout=60)
    return r.status_code, r.text[:600]

print(q("select policyname, count(*) from pg_policies where 'mcp_tyler_attend' = any(roles) group by 1"))
if "--apply" not in sys.argv:
    print(sql[:400], "...\n[dry run]"); sys.exit()
print("apply:", q(sql))
print(q("select policyname, count(*) from pg_policies where 'mcp_tyler_attend' = any(roles) group by 1"))
import psycopg
dsn = dict(l.strip().split("=", 1) for l in open("/root/attend/mcp/.env") if "=" in l)["ATTEND_MCP_DSN"].strip('"')
with psycopg.connect(dsn) as c:
    n = c.execute("select count(*) from customers").fetchone()[0]
    ids = c.execute("select id::text from customers").fetchall()
    print("PROOF as role: customers visible =", n, ids)
    assert n == 1 and ids[0][0] == CUSTOMER, "provision failed"
