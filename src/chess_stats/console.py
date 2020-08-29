import click

from . import __version__
from chess_stats.chess_stats import compute_year_summary


@click.command()
@click.version_option(version=__version__)
def main():
    summary = compute_year_summary("jjjulio", 2020)
    print(f"wins {summary.wins}, losses {summary.losses}, draws {summary.draws}")


if __name__ == "__main__":
    main()
