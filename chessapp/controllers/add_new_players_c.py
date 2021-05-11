
from datetime import datetime

from tinydb import where

from chessapp.models.db_logic_m import DataBase
from chessapp.models.player_m import Player
from chessapp.views.add_new_players_v import AddPlayersViews
from chessapp.controllers import menus_c


class AddNewPlayerController:
    """
    For all new player this controller will ask player's information to the user
    (family_name, first_name, date_of_birth, gender, ranking)
    Then checking if this new player doesn't already exists in database.
    If not, this player will be added to the current tournament and save in data base.
    Add players comes after the user had create a tournament.
    A player will be a Player() instance.
    """

    def __init__(self, current_tournament):
        self.player = Player()
        self.view = AddPlayersViews()
        self.check_1 = True
        self.check_2 = True
        self.check_3 = True
        self.tournament = current_tournament
        self.db = DataBase()

    def __call__(self):

        # FIRST MESSAGE.
        self.view.welcome()

        # CHECKING IF PLAYER ALREADY IN DATA BASE.
        while self.check_3:

            # FAMILY NAME.
            self.view.player_family_name()
            while self.check_1:
                answer = input(">> ")
                if answer.isalpha():
                    test = answer.replace(" ", "")
                    if len(answer) == 0 or len(test) == 0:
                        self.view.special_answer()
                    else:
                        self.player.family_name = answer.upper()
                        self.check_1 = False
                else:
                    self.view.special_answer()
            self.check_1 = True

            # FIRST NAME.
            self.view.player_first_name()
            while self.check_1:
                answer = input(">> ")
                if answer.isalpha():
                    test = answer.replace(" ", "")
                    if len(answer) == 0 or len(test) == 0:
                        self.view.special_answer()
                    else:
                        self.player.first_name = answer.capitalize()
                        self.check_1 = False
                else:
                    self.view.special_answer()
            self.check_1 = True

            # DATE OF BIRTH.
            while self.check_1:
                self.view.player_date_birth()

                day = self._loop_date("DU JOUR DE NAISSANCE", val_max=31, _format="dd")
                month = self._loop_date("DU MOIS DE NAISSANCE", val_max=12, _format="mm")
                year = self._loop_date("DE L'ANNÉE DE NAISSANCE", val_max=float("inf"), _format="yyyy", gender="e")

                try:
                    datetime(int(year), int(month), int(day))
                    self.player.date_of_birth = f"{day}/{month}/{year}"
                    self.check_1 = False
                except ValueError:
                    self.view.wrong_dates()
                    self.check_1 = True
            self.check_1 = True

            # GENDER.
            self.view.player_gender_1()
            while self.check_1:
                self.view.player_gender_2()
                answer = input(">> ")
                if answer == "1":
                    self.player.gender = 'Homme'
                    self.check_1 = False
                elif answer == "2":
                    self.player.gender = 'Femme'
                    self.check_1 = False
                else:
                    self.view.error_gender()
            self.check_1 = True

            # RANKING.
            self.view.player_ranking_1()
            while self.check_1:
                self.view.player_ranking_2()
                self.view.ranking_suggestion()
                answer = input(">> ")
                if answer.upper() == 'C':
                    if len(self.db.players_table) > 0:
                        list_player_db = []
                        for player in self.db.players_table:
                            instance_player = self.db.retrieve_player(player)
                            list_player_db.append(instance_player)
                        list_player_db.sort(key=lambda x: x.ranking)
                        self.view.show_global_ranking(list_player_db)
                    else:
                        self.view.no_players_db()
                else:
                    try:
                        if int(answer) > 0:
                            if self.db.players_table.contains(where("ranking") == answer):
                                self.view.ranking_exists()
                                self.check_2 = True
                                while self.check_2:
                                    self.view.ranking_exists_keep()
                                    answer_2 = input(">> ")
                                    if answer_2.upper() == 'O':
                                        self.player.ranking = answer
                                        self.check_2 = False
                                        self.check_1 = False
                                    elif answer_2.upper() == 'N':
                                        self.check_2 = False
                                    else:
                                        self.view.error_yes_no()
                            else:
                                self.view.ranking_ok()
                                self.player.ranking = answer
                                self.check_1 = False
                        else:
                            self.view.positive_value_needed()
                    except ValueError:
                        self.view.positive_value_needed()
            self.check_1 = True
            if self.db.players_table.contains((where('family_name') == self.player.family_name)
                                              & (where('first_name') == self.player.first_name)
                                              & (where('date_of_birth') == self.player.date_of_birth)
                                              & (where('gender') == self.player.gender)):
                self.view.already_in_db()
                self.view.welcome_already()
                return menus_c.AddPlayerMenuController(self.tournament)
            else:
                self.check_3 = False
        self.tournament.add_player(self.player)
        self.db.save_player(self.player)
        self.db.save_tournament(self.tournament)
        self.view.saving_state()
        self.view.saving_player()
        return menus_c.AddPlayerMenuController(self.tournament)

    # Optimisation format date_of_birth.
    def _loop_date(self, d_m_y, val_max, _format, gender=""):
        self.check_2 = True
        needed_var = 0
        self.view.loop_date_birth(d_m_y, gender, _format, val_max)
        while self.check_2:
            inp_d_m_y = input(">> ")
            try:
                if 10 <= int(inp_d_m_y) <= val_max:
                    needed_var = str(inp_d_m_y)
                    self.check_2 = False
                elif 9 >= int(inp_d_m_y) >= 1 == len(inp_d_m_y):
                    needed_var = f"0{str(inp_d_m_y)}"
                    self.check_2 = False
                elif 9 >= int(inp_d_m_y) >= 1 and len(inp_d_m_y) == 2:
                    needed_var = str(inp_d_m_y)
                    self.check_2 = False
                else:
                    self.view.error_loop_date_birth(val_max, _format)
            except ValueError:
                self.view.error_loop_date_birth(val_max, _format)
        return needed_var


class AddPlayerFromDataController:
    """
    If the user wants to add a players to a tournament from database (table "players")
    this controller will deserialize it and add it to the current tournament.
    """

    def __init__(self, current_tournament,  data_player):
        self.tournament = current_tournament
        self.data_player = data_player
        self.db = DataBase()

    def __call__(self):
        player = self.db.retrieve_player(self.data_player)
        self.tournament.add_player(player)
        return menus_c.AddPlayerMenuController(self.tournament)
