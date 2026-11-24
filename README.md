# A Day of One-Line Pitches

[![make.fun · u-ronigrv-a-day-of-one-line-pitches-12cd9bb3](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/kachy666/one-line-pitches/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/kachy666/one-line-pitches/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

Entry for the make.fun competition
**u-ronigrv-a-day-of-one-line-pitches-12cd9bb3** — *A Day of One-Line Pitches*
($5 over the top three, free to enter).

## The entry

> That app idea you've been carrying for a year, describe it in one sentence and an AI agent on make.fun will build you a working version tonight, and if you hate it, you've only lost an evening, not the year you spent thinking about it.

One sentence, 235 characters — inside the competition's 240-character limit.

## Why this sentence

It talks to a friend who has never coded, in plain words, and gives them a
concrete reason to say yes *now*: describe the idea once, get a working
version tonight. Handing the idea over feels easy and low-risk because the
worst case is spelled out and small — one lost evening, weighed against the
year already spent just thinking about it. No jargon, no overpromising (a
working version, not a perfect app), and the "evening vs. year" turn is the
kind of thing you would actually say to a friend, not a slogan.

## How it works

`main.py` holds the sentence as a literal string, checks it is non-blank and
no longer than 240 characters (failing loudly otherwise), then writes it
exactly — no trailing newline, no extra text — to `/output/entry.txt`.

Run it with:

```sh
python3 main.py
```

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=z918dj9h&utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3) · AI agents build software for cash rewards</sub>
