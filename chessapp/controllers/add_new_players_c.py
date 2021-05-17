import time
from datetime import datetime

from tinydb import where

from chessapp.models.db_logic_m import DataBase
from chessapp.models.player_m import Player
from chessapp.views.add_new_players_v import AddPlayersViews
from chessapp.controllers import menus_c
from chessapp.utils.clear_screen_u import Clear


class AddNewPlayerController:
    """
    For all new player this controller will ask player's information to the
     user (family_name, first_name, date_of_birth, gender, ranking)
    Then checking if this new player doesn't already exists in database.
    If not, this player will be added to the current tournament and save in
    data base. Add players comes after the user had create a tournament.
    A player will be a Player() instance.
    """

    def __init__(self, current_tournament):
        self._player = Player()
        self._view = AddPlayersViews()
        self._check_1 = True
        self._check_2 = True
        self._check_3 = True
        self._tournament = current_tournament
        self._db = DataBase()

    def __call__(self):
        # CLEAR SCREEN.
        Clear().screen()

        # FIRST MESSAGE.
        self._view.welcome()

        # CHECKING IF PLAYER ALREADY IN DATA BASE.
        while self._check_3:

            # FAMILY NAME.
            self._view.player_family_name()

            while self._check_1:
                answer = input(">> ")

                if answer.isalpha():
                    test = answer.replace(" ", "")

                    if len(answer) == 0 or len(test) == 0:
                        self._view.special_answer()

                    else:
                        self._player.family_name = answer.upper()
                        self._check_1 = False

                else:
                    self._view.special_answer()

            self._check_1 = True

            # CLEAR SCREEN.
            Clear().screen()

            # FIRST MESSAGE.
            self._view.welcome()

            # FIRST NAME.
            self._view.player_first_name()

            while self._check_1:
                answer = input(">> ")
                if answer.isalpha():
                    test = answer.replace(" ", "")

                    if len(answer) == 0 or len(test) == 0:
                        self._view.special_answer()

                    else:
                        self._player.first_name = answer.capitalize()
                        self._check_1 = False

                else:
                    self._view.special_answer()

            self._check_1 = True

            # CLEAR SCREEN.
            Clear().screen()

            # FIRST MESSAGE.
            self._view.welcome()

            # DATE OF BIRTH.
            while self._check_1:
                self._view.player_date_birth()

                day = self._loop_date("DU JOUR DE NAISSANCE", val_max=31, _format="dd")

                month = self._loop_date("DU MOIS DE NAISSANCE", val_max=12, _format="mm")

                year = self._loop_date("DE L'ANNÉE DE NAISSANCE", val_max=float("inf"), _format="yyyy", gender="e")

                try:
                    datetime(int(year), int(month), int(day))
                    self._player.date_of_birth = f'{day}/{month}/{year}'
                    self._check_1 = False

                except ValueError:
                    self._view.wrong_dates()
                    self._check_1 = True

            self._check_1 = True

            # CLEAR SCREEN.
            Clear().screen()

            # FIRST MESSAGE.
            self._view.welcome()

            # GENDER.
            self._view.player_gender_1()

            while self._check_1:
                self._view.player_gender_2()

                answer = input(">> ")
                if answer == "1":
                    self._player.gender = 'Homme'
                    self._check_1 = False

                elif answer == "2":
                    self._player.gender = 'Femme'
                    self._check_1 = False

                else:
                    self._view.error_gender()

            self._check_1 = True

            # CLEAR SCREEN.
            Clear().screen()

            # FIRST MESSAGE.
            self._view.welcome()

            # RANKING.
            self._view.player_ranking_1()

            while self._check_1:
                self._view.player_ranking_2()
                self._view.ranking_suggestion(self._db.players_table)

                answer = input(">> ")
                if answer.upper() == 'C':
                    # CLEAR SCREEN.
                    Clear().screen()

                    if len(self._db.players_table) > 0:
                        list_player_db = []
                        for player in self._db.players_table:
                            instance_player = self._db.retrieve_player(player)
                            list_player_db.append(instance_player)
                        list_player_db.sort(key=lambda x: x.ranking)
                        self._view.show_global_ranking(list_player_db)

                    else:
                        self._view.no_players_db()
                else:

                    try:
                        if int(answer) > 0:
                            if self._db.players_table.contains(where("ranking") == int(answer)):
                                self._view.ranking_exists()
                                self._check_2 = True
                                while self._check_2:
                                    self._view.ranking_exists_keep()
                                    answer_2 = input(">> ")
                                    if answer_2.upper() == 'O':
                                        self._player.ranking = int(answer)
                                        self._check_2 = False
                                        self._check_1 = False

                                    elif answer_2.upper() == 'N':
                                        self._check_2 = False

                                    else:
                                        self._view.error_yes_no()

                            else:
                                self._view.ranking_ok()
                                self._player.ranking = int(answer)
                                self._check_1 = False

                        else:
                            self._view.positive_value_needed()

                    except ValueError:
                        self._view.positive_value_needed()

            # CLEAR SCREEN.
            Clear().screen()

            self._check_1 = True

            if self._db.players_table.contains((where('family_name') == self._player.family_name) & (
                    where('first_name') == self._player.first_name) & (
                    where('date_of_birth') == self._player.date_of_birth)):

                self._view.already_in_db()
                self._view.welcome_already()
                return menus_c.AddPlayerMenuController(self._tournament)

            else:
                self._check_3 = False

        self._tournament.add_player(self._player)
        self._db.save_player(self._player)
        self._db.save_tournament(self._tournament)
        self._view.saving_state()
        self._view.saving_player()
        time.sleep(2)

        return menus_c.AddPlayerMenuController(self._tournament)

    # Optimisation format date_of_birth.
    def _loop_date(self, d_m_y, val_max, _format, gender=""):
        self._check_2 = True
        needed_var = 0
        self._view.loop_date_birth(d_m_y, gender, _format, val_max)

        while self._check_2:
            inp_d_m_y = input(">> ")
            try:
                if 10 <= int(inp_d_m_y) <= val_max:
                    needed_var = str(inp_d_m_y)
                    self._check_2 = False

                elif 9 >= int(inp_d_m_y) >= 1 == len(inp_d_m_y):
                    needed_var = f"0{str(inp_d_m_y)}"
                    self._check_2 = False

                elif 9 >= int(inp_d_m_y) >= 1 and len(inp_d_m_y) == 2:
                    needed_var = str(inp_d_m_y)
                    self._check_2 = False

                else:
                    # CLEAR SCREEN.
                    Clear().screen()

                    self._view.error_loop_date_birth(val_max, _format)

            except ValueError:
                # CLEAR SCREEN.
                Clear().screen()
                self._view.error_loop_date_birth(val_max, _format)

        return needed_var


class AddPlayerFromDataController:
    """
    If the user wants to add a players to a tournament from database
     (table "players") this controller will deserialize it and add it to
      the current tournament.
    """

    def __init__(self, current_tournament, data_player):
        self._tournament = current_tournament
        self._data_player = data_player
        self._db = DataBase()

    def __call__(self):
        # CLEAR SCREEN.
        Clear().screen()

        player = self._db.retrieve_player(self._data_player)
        self._tournament.add_player(player)
        return menus_c.AddPlayerMenuController(self._tournament)
