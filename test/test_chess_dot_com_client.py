from chess_stats.models.chess_dot_com_client import ChessDotComClient
from .common import read_json_fixture


def test_fetch_games_succeeds(requests_mock):
    response_data = read_json_fixture("games-2020-08.json")
    requests_mock.get("https://api.chess.com/pub/player/jjjulio/games/2020/08", json=response_data)
    cdc = ChessDotComClient()
    cdc.fetch_games("jjjulio", 2020, 8)
    assert requests_mock.called
    assert requests_mock.call_count == 1


def test_build_url_succeeds():
    username = "jjjulio"
    year = 2020
    month = 8
    url = ChessDotComClient().build_url(username, year, month)
    assert "https://api.chess.com/pub/player/jjjulio/games/2020/08" == url
