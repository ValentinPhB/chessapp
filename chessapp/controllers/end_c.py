import time
from datetime import datetime

from tinydb import where

from chessapp.views.end_v import EndScreenView
from chessapp.models.db_logic_m import DataBase
from chessapp.controllers import menus_c
from chessapp.utils.clear_screen_u import Clear


class EndScreenController:
    """
    To quit the application from the HomeMenuController.
    """

    def __init__(self):
        self.view = EndScreenView()

    def __call__(self):
        self.view.quit()


class EndScreenSaveController:
    """
    To quit and save the state of current_tournament in data base.
    """

    def __init__(self, current_tournament):
        self._tournament = current_tournament
        self._db = DataBase()
        self._view = EndScreenView()

    def __call__(self):
        # CLEAR SCREEN.
        Clear().screen()

        self._db.save_tournament(self._tournament)
        self._view.saving_state()

        self._view.quit()


class EndTournamentController:
    """
    Special ending, when the tournament is over.
    this controller will show the ranking of the tournament and ask the user
     to update the global ranking.
    """

    def __init__(self, current_tournament):
        self._tournament = current_tournament
        self._db = DataBase()
        self._view = EndScreenView()
        self._check_1 = True
        self._check_2 = True

    def __call__(self):
        # CLEAR SCREEN.
        Clear().screen()

        # SAVING STATE.
        self._db.save_tournament(self._tournament)
        self._view.saving_state()

        # ADDING DATE_END TO THE CURRENT TOURNAMENT.
        self._add_date_end_tournament()

        # SHOW TOURNAMENT'S RANKING.
        self._tournament.players_tournament.sort(key=lambda x: (- x.point, x.ranking))
        self._view.show_ranking_tournament(self._tournament.players_tournament)

        # ASKING USER TO UPDATE ALL RANK TO PLAYERS IN DATABASE.
        list_player_db = []
        for player in self._db.players_table:
            instance_player = self._db.retrieve_player(player)
            list_player_db.append(instance_player)
        list_player_db.sort(key=lambda x: x.ranking)
        self._view.show_global_ranking(list_player_db)
        self._reset_all_ranking_bdd()
        self._update_ranking_for_all(self._tournament)

        # SAVING TOURNAMENT.
        self._db.save_tournament(self._tournament)
        self._view.saving_state()
        time.sleep(2)
        return menus_c.HomeMenuController()

    def _update_ranking_for_all(self, current_tournament):
        self._view.welcome_assignation_ranking()
        for element in self._db.players_table:
            self._check_1 = True
            while self._check_1:
                self._view.choose_ranking_message(element)
                answer = input(">> ")
                try:
                    value = int(answer)
                    if 0 < value and self._db.players_table.contains(where("ranking") == value):
                        self._view.ranking_exists()
                        self._check_2 = True

                        while self._check_2:
                            self._view.ranking_exists_keep()
                            answer_2 = input(">> ")
                            if answer_2.upper() == 'O':
                                self._db.players_table.update(
                                    {'ranking': value}, ((where('family_name') == element['family_name']) & (
                                        where('first_name') == element['first_name']) & (
                                        where('date_of_birth') == element['date_of_birth'])))

                                for instances_players in current_tournament.players_tournament:
                                    if instances_players.family_name == element['family_name']\
                                            and instances_players.first_name == element['first_name']\
                                            and instances_players.date_of_birth == element['date_of_birth']:
                                        instances_players.ranking = value

                                    else:
                                        pass

                                self._check_2 = False
                                self._check_1 = False

                            elif answer_2.upper() == 'N':
                                self._check_2 = False

                            else:
                                self._view.error_yes_no()

                    elif 0 < value:
                        self._view.ranking_ok()
                        self._db.players_table.update({'ranking': value}, (
                            (where('family_name') == element['family_name']) & (
                                where('first_name') == element['first_name']) & (
                                where('date_of_birth') == element['date_of_birth'])))

                        for instances_players in current_tournament.players_tournament:
                            if instances_players.family_name == element['family_name']\
                                    and instances_players.first_name == element['first_name']\
                                    and instances_players.date_of_birth == element['date_of_birth']:
                                instances_players.ranking = value

                            else:
                                pass

                        self._check_1 = False
                    else:
                        self._view.positive_value_needed()

                except ValueError:
                    self._view.positive_value_needed()

    def _add_date_end_tournament(self):
        self._tournament.date_end = datetime.now().date().strftime("%d/%m/%Y")
        self._view.add_date_tournament()

    def _reset_all_ranking_bdd(self):
        for player in self._db.players_table:
            player_rank = player['ranking']
            self._db.players_table.update({'ranking': 0}, where('ranking') == player_rank)
