import requests


def create_game(res: dict) -> object:
    white_result = res["white"]["result"]
    white_username = res["white"]["username"]
    white_rating = res["white"]["rating"]
    black_result = res["black"]["result"]
    black_username = res["black"]["username"]
    black_rating = res["black"]["rating"]

    white_player = Player(
        username=white_username, rating=white_rating, result=white_result
    )
    black_player = Player(
        username=black_username, rating=black_rating, result=black_result
    )

    game = Game(
        url=res["url"],
        pgn=res["pgn"],
        time_control=res["time_control"],
        time_class=res["time_class"],
        end_time=res["end_time"],
        is_rated=res["rated"],
        fen=res["fen"],
        rules=res["rules"],
        white=white_player,
        black=black_player,
    )
    return game


def parse_pgn(pgn_string: str) -> dict:
    # TODO
    pass


class ChessDotComAdapter:
    """
    TODO
    """

    def __init__(self):
        self.base_url = "https://api.chess.com/pub"
        self.client = requests.Session()

    def fetch_games(self, username: str) -> list:
        """
        TODO
        :param username:
        :return:
        """
        url = self.build_url(username)
        res = self.client.get(url)
        res.raise_for_status()
        res_json = res.json()
        games = [create_game(raw_game) for raw_game in res_json["games"]]
        return games

    def build_url(self, username: str) -> str:
        """
        TODO
        :param username:
        :return:
        """
        return self.base_url + f"/player/{username}/games/2020/07"


class Player:
    """
    TODO
    """

    def __init__(self, rating=None, username=None, result=None):
        self.rating = rating
        self.username = username
        self.result = result


class Game:
    """
    TODO
    """

    def __init__(
        self,
        url=None,
        pgn=None,
        time_control=None,
        end_time=None,
        is_rated=None,
        fen=None,
        time_class=None,
        rules=None,
        white=None,
        black=None,
    ):

        # Default value for players
        white = Player() if white is None else white
        black = Player() if black is None else black

        self.url = url
        self.pgn = pgn
        self.time_control = time_control
        self.time_class = time_class
        self.end_time = end_time
        self.is_rated = is_rated
        self.fen = fen
        self.rules = rules
        self.white = white
        self.black = black

    def get_winner(self) -> object:
        """Get the winner of the game

        :return: The winning player or None if no winner
        """
        if self.white.result == "win":
            return self.white
        elif self.black.result == "win":
            return self.black
        else:
            return None

    def get_loser(self) -> object:
        """
        TODO
        :return:
        """
        winner = self.get_winner()
        if winner is None:
            return None
        return self.white if winner.username == self.black.username else self.black
