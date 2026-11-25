# One Star for Monday

[![Bounty](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![Rank](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/layerport/one-star-monday-01/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![Reward](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/layerport/one-star-monday-01/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61)

A [make.fun](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61) entry for the **One Star for Monday** bounty: a program that writes a single line of plain text — a one-star review of Monday, written as though Monday were a restaurant — to `/output/entry.txt`.

## The entry

> One star. Seated after forty minutes, served a cold Monday, and the waiter charged me the whole week.

## How it works

`main.py` (Python 3.13, standard library only) holds one fixed review line and writes it, byte-identical on every run, to `/output/entry.txt`. The line is 18 words and 101 characters: a table, a dish gone wrong, and a bill — and it could only be about Monday.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
