
from tinydb import where

from chessapp.models.db_logic_m import DataBase
from chessapp.views.update_ranking_v import UpdateRankingView
from chessapp.controllers import menus_c


class UpdateRankingController:
    """
    When during the tournament,
     the user wants to update a ranking for players and has already chose witch one this controller will ask him for
      the new rank and avert him if the value is already in database for an other player.
      The user is free to assign a ranking witch is already taken by an other player is data base.
      This controller will ask him if he wants to.
    """

    def __init__(self, current_tournament, player_instance_match):
        self.db = DataBase()
        self.view = UpdateRankingView()
        self.player_instance_match = player_instance_match
        self.tournament = current_tournament
        self.check_1 = True

    def __call__(self):
        while self.check_1:
            self.view.welcome(self.player_instance_match)
            answer = input(">> ")

            # SHOW THE GLOBAL RANKING FOR HELP THE USER.
            if answer.upper() == 'C':
                list_player_db = []
                for player in self.db.players_table:
                    instance_player = self.db.retrieve_player(player)
                    list_player_db.append(instance_player)
                list_player_db.sort(key=lambda x: int(x.ranking))
                self.view.show_global_ranking(list_player_db)
            else:
                try:

                    # CHECKING FOR POSITIVE VALUE.
                    if int(answer) > 0:
                        if self.db.players_table.contains(where("ranking") == answer):
                            self.view.ranking_exists()
                            self.check_2 = True
                            while self.check_2:
                                self.view.ranking_exists_keep()
                                answer_2 = input(">> ")

                                # ASK USER IF HE WANTS TO ASSIGN A VALUE WHO ALREADY EXISTS FOR AN OTHER PLAYER.
                                if answer_2.upper() == 'O':
                                    self.view.ranking_ok()

                                    # UPDATE RANKING IN DATABASE.
                                    self.db.players_table.update(
                                        {'ranking': answer},
                                        ((where('family_name') == self.player_instance_match.family_name)
                                         & (where('first_name') == self.player_instance_match.first_name)
                                         & (where('date_of_birth') == self.player_instance_match.date_of_birth)))
                                    for instances_players in self.tournament.players_tournament:
                                        if instances_players.family_name == self.player_instance_match.family_name\
                                                and instances_players.first_name ==\
                                                self.player_instance_match.first_name\
                                                and instances_players.date_of_birth\
                                                == self.player_instance_match.date_of_birth:
                                            instances_players.ranking = answer
                                        else:
                                            pass
                                    self.check_2 = False
                                    self.check_1 = False
                                elif answer_2.upper() == 'N':
                                    self.check_2 = False
                                else:
                                    self.view.error_yes_no()
                        else:
                            # UPDATE RANKING IN DATABASE.
                            self.view.ranking_ok_and_free()
                            self.db.players_table.update(
                                {'ranking': answer}, ((where('family_name') == self.player_instance_match.family_name)
                                                      & (where('first_name') == self.player_instance_match.first_name)
                                                      & (where('date_of_birth') ==
                                                         self.player_instance_match.date_of_birth)))

                            # UPDATE ALSO IN THE PLAYERS TOURNAMENT OF THE CURRENT_TOURNAMENT.
                            for instances_players in self.tournament.players_tournament:
                                if instances_players.family_name == \
                                        self.player_instance_match.family_name \
                                        and instances_players.first_name == \
                                        self.player_instance_match.first_name \
                                        and instances_players.date_of_birth == \
                                        self.player_instance_match.date_of_birth:
                                    instances_players.ranking = answer
                                else:
                                    pass
                            self.check_1 = False
                    else:
                        self.view.positive_value_needed()
                except ValueError:
                    self.view.positive_value_needed()

        return menus_c.SuggestRankingMenuController(self.tournament)
