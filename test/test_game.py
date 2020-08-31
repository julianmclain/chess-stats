from .common import read_json_fixture
from chess_stats.models import Game
from chess_stats.models import Player


def test_winning_player_succeed():
    white = Player(1299, "Jane Doe", "resigned")
    black = Player(1279, "Joana Doe", "win")
    game = Game(white_player=white, black_player=black)
    assert game.winning_player == black


def test_losing_player_succeeds():
    white = Player(1299, "Jane Doe", "resigned")
    black = Player(1279, "Joana Doe", "win")
    game = Game(white_player=white, black_player=black)
    assert game.losing_player == white


def test_from_json():
    game_json = read_json_fixture("game.json")
    url = game_json["url"]
    pgn = game_json["pgn"]
    time_control = game_json["time_control"]
    time_class = game_json["time_class"]
    end_time = game_json["end_time"]
    is_rated = game_json["rated"]
    fen = game_json["fen"]
    rules = game_json["rules"]
    white_username = game_json["white"]["username"]
    black_username = game_json["black"]["username"]
    game_result = Game.from_json(game_json)
    assert url == game_result.url
    assert pgn == game_result.pgn
    assert time_control == game_result.time_control
    assert time_class == game_result.time_class
    assert end_time == game_result.end_time
    assert is_rated == game_result.is_rated
    assert fen == game_result.fen
    assert rules == game_result.rules
    assert white_username == game_result.white_player.username
    assert black_username == game_result.black_player.username
