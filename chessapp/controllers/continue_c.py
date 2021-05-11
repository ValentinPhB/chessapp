
from chessapp.models.db_logic_m import DataBase
from chessapp.controllers import menus_c


class ContinueTournamentController:
    """
    This controller referring the user in function of the state of
    the current tournament.
    """

    def __init__(self, dict_tournament):
        self.dict_tournament = dict_tournament
        self.db = DataBase

    def __call__(self):

        tournament = self.db.retrieve_tournament(self.dict_tournament)

        # CHECKING IF ALL PLAYERS HAVE BEEN ADDED.
        # IF NOT YET.
        if 0 <= len(tournament.players_tournament) < 8:
            return menus_c.AddPlayerMenuController(tournament)

        # IF YES.
        elif len(tournament.players_tournament) == 8:
            return menus_c.SuggestRankingMenuController(tournament)
