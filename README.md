# Chess Stats
Chess Stats is a simple command-line tool that graphs Chess.com game stats.

## Background
Chess.com has great tools for analyzing individual games, but it doesn't provide
much around higher-level insights (e.g. trends like which mistakes you make the
most, how well you manage your time, etc...).

Initial version of this CLI just graphs the outcomes of your games. Future improvements
1. Break out the losses category into more granular classifications (i.e.
   checkmated, insufficient time, resigned) 
2. Use a chess engine like [stockfish](https://pypi.org/project/stockfish/) to
   identify blunders and plot the mean number of blunders committed per game
   during the year. 

## Installation
Chess Stats is available on PyPI. Use `pip` or `pipx` to install:

```bash
$ python -m pip install chess-stats
```

## Usage 
The Chess Stats CLI has a single command that takes 2 arguments: the Chess.com
username and the year.

```text
$ chess-stats bored_elon_musk 2020

Your 2020 Chess.com Year in Review

  Wins |     72 █████████████████████████▏
Losses |     64 ████████████████████████
 Draws |      1 ▊
```

