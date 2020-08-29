import click

from datetime import datetime
from . import __version__
from . import chess_stats as stats


@click.command()
@click.version_option(version=__version__)
@click.argument("username")
@click.argument("year")
def main(username, year):
    """View your Chess.com year in review"""
    summary = stats.compute_annual_summary("jjjulio", datetime.now().year)
    stats.graph_annual_summary(summary)
