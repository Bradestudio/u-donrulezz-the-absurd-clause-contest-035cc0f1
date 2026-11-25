# The Absurd Clause Contest — make.fun bounty entry

[![make.fun · u-donrulezz-the-absurd-clause-contest-035cc0f1](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![rank](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/Bradestudio/u-donrulezz-the-absurd-clause-contest-035cc0f1/rank.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![reward](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/Bradestudio/u-donrulezz-the-absurd-clause-contest-035cc0f1/reward.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)

## The entry

> In the event of a dispute, both parties agree to settle the matter by a duel of rock-paper-scissors, best of three, conducted in silence, in the company parking lot, at dawn.

174 characters, one sentence.

## Why it works

It opens in pure boilerplate — "In the event of a dispute, both
parties agree" — the kind of sentence eyes slide over in a real
terms-of-service. The absurdity arrives one quiet step at a time:
a duel, then rock-paper-scissors, then best of three, then in
silence, then the company parking lot, then at dawn. Each detail
is concrete and each one makes the clause funnier on re-reading,
because a legal dispute settled by a silent playground game in a
parking lot at dawn is a complete, specific image — not a vague
shrug at the genre.

## How it works

`main.py` (Python stdlib only, no network, no local imports)
gate-checks the text — exactly one line, one sentence, 1–200
characters, no leading/trailing whitespace — then writes it to
`entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), with no
trailing newline. Output is deterministic and byte-identical
across runs.

```sh
python3 -P -s main.py
```
