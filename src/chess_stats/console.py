import click

from datetime import datetime
from . import __version__
from . import chess_stats as stats


@click.command()
@click.version_option(version=__version__)
def main():
    # TODO take username as param
    summary = stats.compute_annual_summary("jjjulio", datetime.now().year)
    stats.graph_annual_summary(summary)


if __name__ == "__main__":
    main()
