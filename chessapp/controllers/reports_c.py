
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
        self.db = db
        self.view = ReportPlayerViews()

    def __call__(self):
        # CLEAR SCREEN.
        Clear().screen()

        self.view.welcome()

        self.view.display_actors_rank(self.db.players_table)
        self.view.display_actors_alpha(self.db.players_table)
        self.view.finish()

        self.view.stop_up()
        self._prompt()

        return menus_c.ReportMenuController()

    def _prompt(self):
        _pass = input("|         Entrez n'importe quel caractère pour continuer, ou appuyez sur entrée         |")
        self.view.stop_end()
        return _pass


class ReportTournamentController:
    """
        NOT IMPLEMENTED YET.
        """

    def __init__(self, db, dict_tournament):
        self.db = db
        self.view = ReportTournamentViews(dict_tournament)
        self.dict_tournament = dict_tournament

    def __call__(self):
        # CLEAR SCREEN.
        Clear().screen()

        self.view.welcome(self.dict_tournament)
        self.view.all_player_tournament()
        self.view.all_rounds_tournament()
        self.view.finish()

        return menus_c.ReportMenuController()
