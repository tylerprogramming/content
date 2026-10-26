# REA dry run on Hermes.app (2026-10-15)

Target: our own Electron build, `~/.hermes/hermes-agent/apps/desktop/release/mac-arm64/Hermes.app/Contents/Resources/app.asar`. Source is in `~/.hermes/hermes-agent/apps/desktop/electron/`, so every REA claim can be checked against real code.

REA was run with `npx -y rea-agents@latest` (rea 6.5.0). `rea setup` was NOT run, so no Claude/Codex/Hermes config was touched. No Ghidra/Hopper/IDA (`rea doctor` reports them missing; not needed for this path).

## Commands, in order

```bash
npx -y rea-agents@latest doctor
npx -y rea-agents@latest analyze-javascript-application "$ASAR" --format json --full-output
# -> refused: artifact_integrity_mismatch
npx -y rea-agents@latest analyze-javascript-application "$ASAR" --integrity-policy record-and-continue --format json --full-output > hermes-app.json
```

## Beat 1: it refused first

First run failed in 1.2s with `artifact_integrity_mismatch`: `node-pty/prebuilds/darwin-arm64/pty.node` declared sha256 `e6457d66…`, observed `a6713b52…`. Cause: macOS codesigning rewrites unpacked native binaries after the ASAR is written. REA named the cause and the flag to continue. Rerun marks those 2 files "untrusted" in the limitations list.

## Beat 2: what it found (89.7s, 222 MB JSON)

| Measure | Value |
|---|---|
| JS files parsed | 987 (0 parse failures) |
| Modules | 614 |
| AST nodes visited | 4,172,706 |
| Findings | 12,087 |
| Browser windows | 10 |
| contextBridge APIs / exposed members | 1 / 290 |
| IPC literal channels | 254 |
| Main-process handlers | 203 |
| Renderer sends / listeners | 218 / 88 |
| Unpaired renderer sends | 17 |
| Unknowns in semantic graph | 36,876 |
| Limitations listed | 902 (444 are resource caps: semantic node limit 100,000 hit) |
| Confidence / authority | `derived` / `shipped-artifact` |

## Beat 3: checked against the source

- Source has 205 `ipcMain.handle/on/once` channels. REA found 204 of them.
- The 1 it missed, `retirement-fixture:descriptor`, lives in `pool-retirement-live-fixture/`, a test fixture that is not shipped in the build. Correct miss.
- REA found 50 channels my grep did not. 37 are `webContents.send` pushes, 13 are preload `ipcRenderer.invoke` calls (e.g. `hermes:screenshot:capture`). All 50 exist in source. Zero invented.
- External hosts named in the evidence: 0. Network endpoints come back as `endpoint_kind: route`, not URLs. The "what does it send home" audit needs `capture-electron-scenario` (runtime), not this static command.

## What this means for the video

1. The evidence beat is real and checkable: 204 of 205 shipped channels, 0 hallucinated, on screen against the repo.
2. The refusal is a free beat nobody else has: it would not analyze a tampered build until told to.
3. The "unknowns" are huge (36,876) and honest. Good contrast to Nick's "judged by eye".
4. Static mode does not answer "what does it send home". Either drop that beat or do a runtime capture as a second dry run.

Raw output (222 MB) stays in `~/.hermes/cache/scratch/rea-dry/` (pruned after 24h idle).
