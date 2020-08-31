from .models import ChessDotComAdapter
from .models import AnnualSummary
from typing import List, Dict


def create_annual_summary(username: str, year: int) -> AnnualSummary:
    """

    :param username:
    :param year:
    :return:
    """
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


def create_annual_summary_graph(summary: AnnualSummary) -> List[str]:
    """

    :param summary:
    :return:
    """
    graph = []
    title = f"\nYour {summary.year} Chess.com Year in Review\n"
    graph.append(title)

    data = {
        "Wins": summary.wins,
        "Losses": summary.losses,
        "Draws": summary.draws,
    }
    label_space_control = max((len(label) for label in data.keys()))
    value_space_control = max((len(str(value)) for value in data.values())) + 1
    scaled_data = _scale_values(data)
    for label, value in scaled_data.items():
        num_bars, remainder = divmod(value, 8)
        bar = "█" * num_bars
        remainder_bar = chr(ord("█") + remainder)
        bar += remainder_bar
        row = f"{label.rjust(label_space_control)} | {str(value).rjust(value_space_control)} {bar}"
        graph.append(row)

    return graph


def _scale_values(data: Dict[str, int]) -> Dict[str, int]:
    """

    :param data:
    :return:
    """
    graph_max_num_bars = 288  # 36 bars of eighths
    max_data_value = max(data.values())
    if max_data_value > 0:
        scale_factor = graph_max_num_bars / max_data_value
    else:
        return data

    scaled_data = {}
    for label, value in data.items:
        scaled_data[label] = int(value * scale_factor)

    return scaled_data


def print_annual_summary_graph(graph: List[str]) -> None:
    """

    :param graph:
    """
    for row in graph:
        print(row)
