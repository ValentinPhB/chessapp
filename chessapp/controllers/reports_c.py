
from chessapp.controllers import menus_c
from chessapp.views.reports_v import ReportPlayerViews, ReportTournamentViews
from chessapp.utils.clear_screen_u import Clear


class ReportPlayerController:
    """
    This controller display two reports ; all actors in alphabetic order and
     all actors in ranking order.
    The user can consult them, he is also redirect to ReportMenuController.
    """
    def __init__(self, db):
        self._db = db
        self._view = ReportPlayerViews()

    def __call__(self):
        # CLEAR SCREEN.
        Clear().screen()

        self._view.welcome()

        self._view.display_actors_rank(self._db.players_table)
        self._view.display_actors_alpha(self._db.players_table)
        self._view.finish()

        self._view.stop_up()
        self._prompt()

        return menus_c.ReportMenuController()

    def _prompt(self):
        _pass = input("|         Entrez n'importe quel caractère pour continuer, ou appuyez sur entrée         |")
        self._view.stop_end()
        return _pass


class ReportTournamentController:
    """
        NOT IMPLEMENTED YET.
        """

    def __init__(self, db, dict_tournament):
        self._db = db
        self._view = ReportTournamentViews(dict_tournament)
        self._dict_tournament = dict_tournament

    def __call__(self):
        # CLEAR SCREEN.
        Clear().screen()

        self._view.welcome(self._dict_tournament)
        answer = self._view.all_player_tournament()
        if answer.upper() == 'Q':
            return menus_c.ReportMenuController()
        elif answer.upper() != 'Q':
            pass
        self._view.all_rounds_tournament()
        self._view.finish()
        return menus_c.ReportMenuController()
