from requests import Session

from typing import List
from datetime import datetime
from .game import Game


class ChessDotComAdapter:
    """
    TODO
    """

    def __init__(self):
        self.base_url = "https://api.chess.com/pub"
        self.client = Session()

    def fetch_games_for_year(self, username: str, year: int) -> List[Game]:
        """
        :param username:
        :param year:
        :return:
        """
        num_months = datetime.now().month if datetime.now().year == year else 12
        games = []
        for month in range(1, num_months+1):
            url = self.build_url(username, year, month)
            res = self.client.get(url)
            res.raise_for_status()
            res_json = res.json()
            games.extend([Game.from_json(game_json) for game_json in res_json["games"]])
        return games

    def build_url(self, username: str, year: int, month: int) -> str:
        """
        TODO

        The Chess.com API expects a 2 digit month

        :param username:
        :param year:
        :param month:
        :return:
        """
        month_str = str(month) if month / 10 >= 1 else f"0{month}"
        return self.base_url + f"/player/{username}/games/{year}/{month_str}"

    def parse_pgn(self, pgn_string: str) -> dict:
        # TODO
        pass
