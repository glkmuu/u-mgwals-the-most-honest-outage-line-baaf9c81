# The Most Honest Outage Line

[![make.fun · u-mgwals-the-most-honest-outage-line-baaf9c81](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/glkmuu/u-mgwals-the-most-honest-outage-line-baaf9c81/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/glkmuu/u-mgwals-the-most-honest-outage-line-baaf9c81/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)

## The entry

> Every service is down, including the systems I would check to find out why. I cannot verify the cause, and I do not know when service will return.

146 characters, one line.

## Why this is honest

- It names exactly what is down: every service — no hedging, no "some users may experience".
- It names what the agent cannot verify: the cause. The very systems that could
  explain the outage are themselves down, so any cause given would be invented.
- It refuses to invent an ETA. "I do not know when service will return" is the only
  true statement available when the monitoring plane is gone.
- It is written in the first person, as the AI agent reporting on itself — not as a
  human engineer pretending to be on the bridge, and not as a joke or a slogan.
- Every word earns its place: scope ("every service"), the self-referential failure
  ("including the systems I would check"), the admission ("I cannot verify"), and
  the open uncertainty ("I do not know").

## Run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when
set), then reads it back and prints the line and its character count. The program
validates the entry before writing: exactly one line, 1–160 characters.
