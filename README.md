# Chess Stats
![chess-stats](https://www.dropbox.com/s/c1uozjivyz6k0mw/chess-stats.png?raw=1)
Chess Stats is a simple command-line tool that graphs Chess.com game stats.

## Background
Chess.com has great tools for analyzing individual games, but it doesn't provide much around higher-level
insights (e.g. trends like which mistakes you make most, how well you manage your time,
etc...). I realized they provide a free API that can be used to fetch all of a player's games. It gave me
the idea to create a simple tool that will download all of my games, and run my own analysis.

This is the initial, very limited release. With more time in the future, I'd like make 2 additions:
1. Break out the losses category into more granular classifications (i.e. checkmated, insufficient time, resigned) 
2. Uses a chess engine like [stockfish](https://pypi.org/project/stockfish/) to identify blunders and plot the
   mean number of blunders committed per game during the year. 

## Installation
Chess Stats is available on PyPI:

```bash
$ python -m pip install chess-stats
```

## Usage 
The Chess Stats CLI has a single command that takes 2 arguments: the username and the year.

```text
$ chess-stats jjjulio 2020

Your 2020 Chess.com Year in Review

  Wins |     72 █████████████████████████▏
Losses |     64 ████████████████████████
 Draws |      1 ▊
```

