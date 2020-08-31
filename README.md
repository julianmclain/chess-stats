# Chess Stats

Chess Stats is a simple command-line tool that graphs Chess.com game stats.

## Background
I play a lot of games on Chess.com. The platform has good tools for analyzing each game, but the st I wanted a quick way to understand my stats. Chess.com gives you a lot of great tools for individual games, but there isn't much for larger trends

## Installation
Chess Stats is available on PyPI:

```bash
$ python -m pip install chess-stats
```

## Usage 
From the terminal, run the executable with a Chess.com username and a year:

```text
$ chess-stats jjjulio 2020

Your 2020 Chess.com Year in Review

  Wins |     72 █████████████████████████▏
Losses |     64 ████████████████████████
 Draws |      1 ▊
```

TODO
- docstrings (requests for inspo)
- test
- README 
- pypi
- beef up how requests are made (e.g. timeouts)
