from .common import read_json_fixture
from chess_stats.models import AnnualSummary, ChessDotComClient
from chess_stats.chess_stats import (
    create_annual_summary,
    create_annual_summary_graph,
    fetch_games_for_year,
)


def test_fetch_games_for_previous_year_succeeds(requests_mock):
    response_json = read_json_fixture("games.json")
    username = "jjjulio"
    year = 2019
    for i in range(1, 13):
        requests_mock.get(ChessDotComClient.build_url(username, year, i), json=response_json)
    fetch_games_for_year(username, year)
    requests_mock.called
    assert requests_mock.call_count == 12


def test_create_annual_summary_succeeds(requests_mock):
    response_json = read_json_fixture("games.json")
    username = "jjjulio"
    year = 2019
    for i in range(1, 13):
        requests_mock.get(ChessDotComClient.build_url(username, year, i), json=response_json)
    summary = create_annual_summary(username, year)
    assert summary.wins == 12
    assert summary.losses == 12
    assert summary.draws == 12


def test_create_annual_summary_graph_small_succeeds():
    summary = AnnualSummary(2020, 72, 64, 1)
    expected_graph = [
        "\nYour 2020 Chess.com Year in Review\n",
        "  Wins |  72 █████████████████████████████████████",
        "Losses |  64 █████████████████████████████████",
        " Draws |   1 ▌",
    ]
    graph = create_annual_summary_graph(summary)
    assert expected_graph == graph


def test_create_annual_summary_graph_large_succeeds():
    summary = AnnualSummary(2018, 296, 195, 9)
    expected_graph = [
        "\nYour 2018 Chess.com Year in Review\n",
        "  Wins |  296 █████████████████████████████████████",
        "Losses |  195 ███████████████████████▍",
        " Draws |    9 ██",
    ]
    graph = create_annual_summary_graph(summary)
    assert expected_graph == graph
