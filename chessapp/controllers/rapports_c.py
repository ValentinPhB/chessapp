
from chessapp.controllers import menus_c
from chessapp.views.rapports_v import RapportPlayerViews,\
    RapportTournamentViews


class RapportPlayerController:
    """
    This controller display two rapports ; all actors in alphabetic order and
     all actors in ranking order.
    The user can consult them, he is also redirect to RapportMenuController.
    """
    def __init__(self, db):
        self.db = db
        self.view = RapportPlayerViews()

    def __call__(self):
        self.view.welcome()

        self.view.display_actors_rank(self.db.players_table)
        self.view.display_actors_alpha(self.db.players_table)
        self.view.finish()
        return menus_c.RapportMenuController()


class RapportTournamentController:
    """
        NOT IMPLEMENTED YET.
        """

    def __init__(self, db, dict_tournament):
        self.db = db
        self.view = RapportTournamentViews(dict_tournament)
        self.dict_tournament = dict_tournament

    def __call__(self):
        self.view.welcome()
        self.view.all_player_tournament()
        self.view.all_rounds_tournament()
        self.view.finish()
        return menus_c.RapportMenuController()
