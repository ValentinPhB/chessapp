import time

from tinydb import where

from chessapp.models.db_logic_m import DataBase
from chessapp.views.update_ranking_v import UpdateRankingView
from chessapp.controllers import menus_c
from chessapp.utils.clear_screen_u import Clear


class UpdateRankingController:
    """
    When during the tournament,
     the user wants to update a ranking for players and has already chose
      witch one this controller will ask him for the new rank and avert him if
       the value is already in database for an other player.
      The user is free to assign a ranking witch is already taken by an other
       player is data base.
      This controller will ask him if he wants to.
    """

    def __init__(self, current_tournament, player_instance_match):
        self._db = DataBase()
        self._view = UpdateRankingView()
        self._player_inst = player_instance_match
        self._tournament = current_tournament
        self._check_1 = True
        self._check_2 = True

    def __call__(self):
        # CLEAR SCREEN.
        Clear().screen()

        while self._check_1:
            self._view.welcome(self._player_inst)

            answer = input(">> ")

            # SHOW THE GLOBAL RANKING FOR HELP THE USER.
            if answer.upper() == 'C':
                list_player_db = []

                for player in self._db.players_table:
                    instance_player = self._db.retrieve_player(player)
                    list_player_db.append(instance_player)

                list_player_db.sort(key=lambda x: int(x.ranking))
                self._view.show_global_ranking(list_player_db)

            else:
                try:

                    # CHECKING FOR POSITIVE VALUE.
                    if int(answer) > 0:
                        if self._db.players_table.contains(where("ranking") == int(answer)):
                            self._view.ranking_exists()
                            self._check_2 = True

                            while self._check_2:
                                self._view.ranking_exists_keep()
                                answer_2 = input(">> ")

                                # ASK USER IF HE WANTS TO ASSIGN A VALUE
                                # WHO ALREADY EXISTS FOR AN OTHER PLAYER.
                                if answer_2.upper() == 'O':
                                    self._view.ranking_ok()

                                    # UPDATE RANKING IN DATABASE.
                                    self._db.players_table.update({'ranking': int(answer)}, (
                                        (where('family_name') == self._player_inst.family_name) & (
                                            where('first_name') == self._player_inst.first_name) & (
                                            where('date_of_birth') == self._player_inst.date_of_birth)))

                                    for inst_play in self._tournament.players_tournament:
                                        if inst_play.family_name == self._player_inst.family_name\
                                                and inst_play.first_name == self._player_inst.first_name\
                                                and inst_play.date_of_birth == self._player_inst.date_of_birth:

                                            inst_play.ranking = int(answer)

                                        else:
                                            pass
                                    self._check_2 = False
                                    self._check_1 = False

                                elif answer_2.upper() == 'N':
                                    self._check_2 = False

                                else:
                                    self._view.error_yes_no()

                        else:
                            # UPDATE RANKING IN DATABASE.
                            self._view.ranking_ok_and_free()
                            time.sleep(2)
                            self._db.players_table.update({'ranking': int(answer)}, (
                                (where('family_name') == self._player_inst.family_name) & (
                                    where('first_name') == self._player_inst.first_name) & (
                                    where('date_of_birth') == self._player_inst.date_of_birth)))

                            # UPDATE ALSO IN THE PLAYERS TOURNAMENT OF THE
                            # CURRENT_TOURNAMENT.
                            for inst_play in self._tournament.players_tournament:
                                if inst_play.family_name == self._player_inst.family_name\
                                        and inst_play.first_name == self._player_inst.first_name \
                                        and inst_play.date_of_birth == self._player_inst.date_of_birth:
                                    inst_play.ranking = int(answer)

                                else:
                                    pass

                            self._check_1 = False

                    else:
                        self._view.positive_value_needed()

                except ValueError:
                    self._view.positive_value_needed()

        # SAVE ACTUAL STATE.
        self._db.save_tournament(self._tournament)
        self._view.saving_state()
        time.sleep(2)

        return menus_c.SuggestRankingMenuController(self._tournament)
