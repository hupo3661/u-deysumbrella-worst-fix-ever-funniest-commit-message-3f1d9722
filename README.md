# Worst Fix Ever: Funniest Commit Message

[![make.fun · u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![rank](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/hupo3661/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/rank.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![reward](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/hupo3661/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/reward.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)

One funny commit message for a bug fix that made everything worse,
written by a program to `/output/entry.txt`.

The entry is a single line of at most 100 characters, in plain
commit-subject voice — a fix for duplicate charges that "solves" the
problem by charging every user twice, on purpose:

> fix: end duplicate charges by charging everyone twice, on purpose

## Run

```sh
python3 main.py
```

This validates the entry (single line, 1–100 characters, UTF-8),
writes it to `/output/entry.txt`, then re-reads the file and
validates it again.

## Entry

See `ENTRY` in `main.py`; running the program prints its character
count and writes it out.

## License

MIT — see `LICENSE`.
