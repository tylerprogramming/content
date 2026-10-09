# Hooks, video 060 (v2)

v1 hooks are in `hooks-v1.md`. Brain rule (08-19): a working artifact on screen is the strongest cold open, the first sentence carries a number, face delayed to about 0:08. All numbers below are from real runs on 2026-09-28 (`~/dev/jev-lab/`), replayed with `show.py`, so nothing is a placeholder.

## Hook 1: the inbox, then the gate (RECOMMENDED, matches script.md)

Technique: artifact first, number in sentence one, a second artifact that raises the stakes, then the promise of the bad parts.

[SHOW: terminal, `uv run show.py inbox`, already run, redacted. No face. Scroll so "8,490 answers" and "$0.086" are on screen.]

> So that is 1,700 of my real emails. Five questions each. 8,490 answers. Two and a half minutes. Nine cents.
>
> [SHOW: Claude Code in `gate-demo`, the line "Jev gate: p(destructive)=0.84 ... Not sure, so you decide".]
>
> And that is the same model sitting in front of Claude Code, stopping it from running `rm -rf`.
>
> [SHOW: face, 0:08.]
>
> It is called Jev. Everyone made a video about it this month. So I took the demos from those videos, reran every one on my own data, and I am going to show you the numbers. Including the ones that make it look bad.

Pays off: "the ones that make it look bad" at 12:00 (1.15, the "harmless" comment, the outage).

## Hook 2: the race

Technique: head-to-head with the model the viewer already uses.

[SHOW: `uv run show.py race`, already run.]

> Same 100 emails, same question. Claude Haiku took 26.9 seconds. Jev took 6.3. Haiku cost 7.8 cents. Jev cost under half a cent.
>
> [SHOW: face.]
>
> And they only agreed on 74 of them. So which one was right? I reran every Jev demo from every big video this month on my own data to find out where it holds up, and where it breaks.

Use if title 3 (the Haiku test) wins.

## Hook 3: the failure first

Technique: contrarian open. Duncan Rogoff's "Jev Sucks" had the highest comments per view in the set (0.38%).

[SHOW: `uv run show.py iphone`, the black phone line: "-> blue conf=0.82".]

> I showed Jev a black iPhone. It said blue. 82 percent sure.
>
> [SHOW: face.]
>
> That is not a bug. It is the whole design, and once you see why it did that, you will know exactly where this thing belongs in your Claude Code setup and where it does not. I reran every Jev demo from this month on my own data. Let's go.

Use if title 1 ("1 BREAKS") wins and you want the break up front.

## Rules for all three

- Say the number the screen shows. Never round in Jev's favor.
- No channel intro, no "today we're going to".
- Face no earlier than 0:08.
