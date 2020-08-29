from .models import ChessDotComAdapter
from .models import AnnualSummary


def compute_year_summary(username: str, year: int) -> AnnualSummary:
    cdc = ChessDotComAdapter()
    games = cdc.fetch_games_for_year(username, year)
    wins = 0
    losses = 0
    draws = 0
    for game in games:
        if game.winning_player is None:
            draws += 1
        elif game.losing_player.username == username:
            losses += 1
        else:
            wins += 1

    return AnnualSummary(wins, losses, draws)
