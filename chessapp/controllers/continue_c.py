
from chessapp.models.db_logic_m import DataBase
from chessapp.controllers import menus_c
from chessapp.utils.clear_screen_u import Clear
from chessapp.controllers.rounds_c import RoundMakerController


class ContinueTournamentController:
    """
    This controller referring the user in function of the state of
    the current tournament.
    """

    def __init__(self, dict_tournament):
        self._dict_tournament = dict_tournament
        self._db = DataBase

    def __call__(self):
        # CLEAR SCREEN.
        Clear().screen()

        tournament = self._db.retrieve_tournament(self._dict_tournament)

        # CHECKING IF ALL PLAYERS HAVE BEEN ADDED.
        # IF NOT YET.
        if 0 <= len(tournament.players_tournament) < 8:
            return menus_c.AddPlayerMenuController(tournament)

        # IF YES.
        elif len(tournament.players_tournament) == 8 and len(tournament.all_round) == 0:
            return RoundMakerController(tournament)

        elif len(tournament.players_tournament) == 8 and len(tournament.all_round) > 0:
            return menus_c.SuggestRankingMenuController(tournament)
