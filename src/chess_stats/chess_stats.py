from .models import ChessDotComAdapter
from .models import AnnualSummary


def compute_annual_summary(username: str, year: int) -> AnnualSummary:
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

    return AnnualSummary(year, wins, losses, draws)


def graph_annual_summary(summary: AnnualSummary) -> None:
    """

    :param summary:
    :return:
    """
    data = {
        "Wins": summary.wins,
        "Losses": summary.losses,
        "Draws": summary.draws,
    }
    max_label_length = max((len(label) for label in data.keys()))
    max_value_length = max((len((str(value))) for value in data.keys()))
    increment = 200 / max(data.values())
    title = f"\nYour {summary.year} Chess.com Year in Review\n"
    print(title)
    for label, value in data.items():
        num_bars, remainder = divmod(int(value * 8 / increment), 8)
        bar = "█" * num_bars
        remainder_bar = chr(ord("█") + remainder)
        bar += remainder_bar
        empty = "▏"
        print(f"{label.rjust(max_label_length)} | {str(value).rjust(max_value_length)} {bar}")
