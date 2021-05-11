
from tinydb import where

from chessapp.utils.menus_u import Menu
from chessapp.views.menus_v import MenuView
from chessapp.controllers.create_tournament_c import CreateTournamentController
from chessapp.controllers.update_ranking_c import UpdateRankingController
from chessapp.controllers.continue_c import ContinueTournamentController
from chessapp.controllers.rapports_c import RapportPlayerController,\
    RapportTournamentController

from chessapp.controllers.end_c import EndScreenController,\
    EndScreenSaveController, EndTournamentController

from chessapp.controllers.add_new_players_c import AddNewPlayerController,\
    AddPlayerFromDataController

from chessapp.controllers.rounds_c import RoundMakerController
from chessapp.controllers.update_results_c import UpdateResultsController
from chessapp.models.db_logic_m import DataBase
from chessapp.models.tournament_m import Tournament


class HomeMenuController:
    """
    This controller display the home menu.
     The user can create a new tournament or continue ones not finished.
     The user can also display rapports, or quit the application.
    """

    def __init__(self):
        self.menu = Menu()
        self.view = MenuView(self.menu)
        self.user_choice = None
        self.check_1 = True
        self.tournament = Tournament()
        self.db = DataBase()

    def __call__(self):

        # ADD MENUS.
        # IF A TOURNAMENT IN DATA BASE IS NOT FINISHED.
        if self.db.tournaments_table.contains(where('date_end')
                                              == str("None")):
            self.menu.add("auto", "Continuer le précédent"
                                  " tournoi non-terminé.",
                          ContinueMenuController(self.tournament))
            self.menu.add("auto", "Afficher des rapports.",
                          RapportMenuController())
            self.menu.add("Q", "Quitter l'application.", EndScreenController())
        else:
            self.menu.add("auto", "Créer un tournoi.",
                          CreateTournamentController(self.tournament))
            self.menu.add("auto", "Afficher des rapports.",
                          RapportMenuController())
            self.menu.add("Q", "Quitter l'application.", EndScreenController())

        # DISPLAY MENU AND GET USER CHOICE.
        self.view.welcome_home()
        while self.check_1:
            self.view.user_choice()
            answer = input(">> ")
            if answer.upper() in self.menu:
                self.user_choice = self.menu[answer.upper()]
                self.check_1 = False
            else:
                self.view.error_entry()
        return self.user_choice.handler


class AddPlayerMenuController:
    """
    This controller will display choices for the user.
     The user can create a new player or retrieve it from the data base.
    """

    def __init__(self, current_tournament):
        self.menu = Menu()
        self.view = MenuView(self.menu)
        self.user_choice = None
        self.check_1 = True
        self.tournament = current_tournament

    def __call__(self):

        # ADD MENUS.
        self.menu.add("auto",
                      "Ajouter un nouveau joueur et le sauvegarder"
                      " dans la base de données.",
                      AddNewPlayerController(self.tournament))
        self.menu.add("auto", "Choisir un joueur dans la base de données.",
                      PlayerDataMenuController(self.tournament))
        self.menu.add("Q", "Sauvegarder et quitter l'application.",
                      EndScreenSaveController(self.tournament))

        # CHECKING IF NUMBER PLAYER < 8 TO REDIRECT PROPERLY.
        players_list = self.tournament.players_tournament
        counting = len(players_list)
        if counting < 8:
            self.view.welcome_add_player(counting)
            while self.check_1:
                self.view.user_choice()
                answer = input(">> ")
                if answer.upper() in self.menu:
                    self.user_choice = self.menu[answer.upper()]
                    self.check_1 = False
                else:
                    self.view.error_entry()
                    self.view.repeat_nbr_remaining(counting)

            return self.user_choice.handler

        else:
            return RoundMakerController(self.tournament)


class PlayerDataMenuController:
    """
    This controller will display all players in data base
     if there are not already chosen in the current tournament.
     The user can chose a player to add it to the tournament.
    """

    def __init__(self, current_tournament):
        self.menu = Menu()
        self.view = MenuView(self.menu)
        self.user_choice = None
        self.check_1 = True
        self.tournament = current_tournament
        self.db = DataBase()

    def __call__(self):

        # SELECTING PLAYERS FROM DATA AND SHOW ONLY THOSE
        # WHO ARE NOT ALREADY CHOSEN.
        # ADDING EVERY PLAYER AS MENUS.
        number_player = self.db.players_table.all()
        if len(number_player) >= 1:
            player_to_show = sorted(
                number_player, key=lambda k: int(k['ranking']))
            if len(self.tournament.players_tournament) > 0:
                for player_instance in self.tournament.players_tournament:
                    family_name = player_instance.family_name

                    first_name = player_instance.first_name

                    date_of_birth = player_instance.date_of_birth

                    ranking = player_instance.ranking

                    if self.db.players_table.contains(
                            (where('family_name') == family_name)
                            & (where('first_name') == first_name)
                            & (where('date_of_birth') == date_of_birth)
                            & (where('ranking') == ranking)):
                        player_to_show[:] = [x for x in
                                             player_to_show if not
                                             ((x.get('family_name')
                                               == family_name)
                                              & (x.get('first_name')
                                                 == first_name)
                                              & (x.get('date_of_birth')
                                                 == date_of_birth)
                                              & (x.get('ranking') == ranking))]
                    else:
                        pass
            else:
                pass

            # CHECKING IF THERE'S AT LEAST ONE PLAYER TO SHOW.
            # IN THAT CASE IT WILL DISPLAY ALL PLAYERS IN THIS LIST.
            # OTHERWISE IT WILL INFORM THE USER AND REDIRECT IT TO
            # 'ADD PLAYER MENU CONTROLLER'.
            if len(player_to_show) != 0:
                for players in player_to_show:
                    self.menu.add("auto", f"    NOM DE FAMILLE : "
                                          f"'{players['family_name']}',"
                                          f" PRÉNOM :"
                                          f" '{players['first_name']}',"
                                          f" DATE DE NAISSANCE :"
                                          f" '{players['date_of_birth']}',"
                                          f" CLASSEMENT GÉNÉRAL :"
                                          f" '{players['ranking']}'.",

                                  AddPlayerFromDataController(
                                      self.tournament, players))

                self.menu.add("\nQ", "  REVENIR AU MENU D'AJOUT DES JOUEURS.",
                              AddPlayerMenuController(self.tournament))
                self.view.welcome_add_from_data()
                while self.check_1:
                    self.view.user_choice()
                    answer = input(">> ")
                    if answer.upper() in self.menu:
                        self.user_choice = self.menu[answer.upper()]
                        self.check_1 = False
                    else:
                        self.view.error_entry()
                return self.user_choice.handler
            else:
                self.view.no_players_db()
                return AddPlayerMenuController(self.tournament)
        else:
            self.view.no_players_db()
            return AddPlayerMenuController(self.tournament)


class ContinueMenuController:
    """
    This controller will display unfinished tournament.
    """

    def __init__(self, current_tournament):
        self.menu = Menu()
        self.view = MenuView(self.menu)
        self.user_choice = None
        self.check_1 = True
        self.db = DataBase()
        self.tournament = current_tournament

    def __call__(self):

        # CHECKING IF THERE'S ONE TOURNAMENT UNFINISHED IN DATA BASE.
        # IN THAT CASE IT WILL DISPLAY IT.
        # OTHERWISE IT WILL INFORM THE USER AND REDIRECT IT TO
        # 'HOME MENU CONTROLLER'.
        if len(self.db.tournaments_table) >= 1:
            for _dict in self.db.tournaments_table:
                if _dict['date_end'] == "None":
                    self.menu.add(
                        "auto", f"    NOM : '{_dict['name']}',"
                                f" LIEU : '{_dict['place']}',"
                                f" DATE DE DEBUT :"f" '{_dict['date_start']}',"
                                f"ROUND(S) JOUÉ(S) :"
                                f" '{len(_dict['all_round'])}' sur"
                                f" '{_dict['nb_total_round']}',"
                                f" NOMBRE DE JOUEURS :"
                                f" '{len(_dict['players_tournament'])}'"
                                f" CONTRÔLE DE TEMPS :"
                                f" '{_dict['control_time']}'.",

                        ContinueTournamentController(_dict))
                else:
                    pass
            self.menu.add("Q", "QUITTER ET REVENIR AU MENU D'ACCUEIL.",
                          HomeMenuController())

            self.view.welcome_continue()
            while self.check_1:
                self.view.user_choice()
                answer = input(">> ")
                if answer.upper() in self.menu:
                    self.user_choice = self.menu[answer.upper()]
                    self.check_1 = False
                else:
                    self.view.error_entry()
            return self.user_choice.handler
        else:
            self.view.no_tournament_db()
            return HomeMenuController()


class RoundMakingMenuController:
    """
    This controller ask the user if he wants to continue or save an quit.
    """

    def __init__(self, current_tournament):
        self.menu = Menu()
        self.view = MenuView(self.menu)
        self.user_choice = None
        self.check_1 = True
        self.tournament = current_tournament

    def __call__(self):

        # ADD MENUS.
        self.menu.add("auto", "Assigner des résultats aux matchs ci-dessus.",
                      UpdateResultsController(self.tournament))
        self.menu.add("Q", "Sauvegarder et quitter l'application.",
                      EndScreenSaveController(self.tournament))

        # DISPLAY MENU AND GET USER CHOICE.
        while self.check_1:
            self.view.user_choice()
            answer = input(">> ")
            if answer.upper() in self.menu:
                self.user_choice = self.menu[answer.upper()]
                self.check_1 = False
            else:
                self.view.error_entry()
        return self.user_choice.handler


class SuggestRankingMenuController:
    """
    This controller ask if the user wants to update player's ranking, continue
     the tournament or save and quit.
    """

    def __init__(self, current_tournament):
        self.menu = Menu()
        self.view = MenuView(self.menu)
        self.tournament = current_tournament
        self.check_1 = True

    def __call__(self):

        # ADD MENUS.
        precedent_round = self.tournament.all_round[-1]
        if precedent_round.matches[0].result_1\
                == precedent_round.matches[0].result_2 == 0.0:

            return RoundMakerController(self.tournament)

        elif int(self.tournament.nb_total_round)\
                == len(self.tournament.all_round)\
                and (precedent_round.matches[0].result_1
                     != precedent_round.matches[0].result_2
                     or precedent_round.matches[0].result_1
                     == precedent_round.matches[0].result_2 == 0.5):

            return EndTournamentController(self.tournament)

        else:
            self.menu.add("auto", "Générer les prochains matchs.",
                          RoundMakerController(self.tournament))
            self.menu.add("auto", "Changer le classement d'un joueur.",
                          UpdateRankingMenuController(self.tournament))
            self.menu.add("Q", "Sauvegarder et quitter l'application.",
                          EndScreenSaveController(self.tournament))

        # DISPLAY MENU AND GET USER CHOICE.
        while self.check_1:
            self.view.user_choice()
            answer = input(">> ")
            if answer.upper() in self.menu:
                self.user_choice = self.menu[answer.upper()]
                self.check_1 = False
            else:
                self.view.error_entry()
        return self.user_choice.handler


class UpdateRankingMenuController:
    """
    This controller will show every players from the current tournament.
     the user will chose witch one he wants to update the global ranking.
    """

    def __init__(self, current_tournament):
        self.menu = Menu()
        self.db = DataBase()
        self.view = MenuView(self.menu)
        self.tournament = current_tournament
        self.check_1 = True

    def __call__(self):

        # WELCOME MESSAGE.
        self.view.welcome_update_global_ranking()

        # ADD MENUS.
        list_player_db = []
        for player in self.db.players_table:
            instance_player = self.db.retrieve_player(player)
            list_player_db.append(instance_player)
        list_player_db.sort(key=lambda x: int(x.ranking))
        for player_instance in list_player_db:
            self.menu.add(
                "auto", f"'{player_instance.family_name}"
                        f" {player_instance.first_name}',"
                        f" né(e) le : '{player_instance.date_of_birth}',"
                        f" classement actuel : '{player_instance.ranking}'.",
                        UpdateRankingController(self.tournament,
                                                player_instance))

        self.menu.add("Q", "Revenir au précédent menu.",
                      SuggestRankingMenuController(self.tournament))

        # DISPLAY MENU AND GET USER CHOICE.
        while self.check_1:
            self.view.user_choice()
            answer = input(">> ")
            if answer.upper() in self.menu:
                self.user_choice = self.menu[answer.upper()]
                self.check_1 = False
            else:
                self.view.error_entry()
        return self.user_choice.handler


class RapportMenuController:
    """
    This controller asks the user to know witch rapports he wants.
    """
    def __init__(self):
        self.menu = Menu()
        self.view = MenuView(self.menu)
        self.db = DataBase()
        self.check_1 = True

    def __call__(self):

        # NO PLAYERS AND TOURNAMENT IN DATA.
        if len(self.db.players_table) == len(self.db.tournaments_table) == 0:
            self.view.none_data()
            return HomeMenuController()
        else:
            self.view.welcome_rapports()

            self.menu.add(
                "auto", "Joueurs enregistrés dans la base de données.",
                        RapportPlayerController(self.db))
            self.menu.add(
                "auto", "Tournois enregistrés dans la base de données.",
                        RapportTournamentMenuController())
            self.menu.add("Q", "Revenir au précédent menu.",
                          HomeMenuController())

        # DISPLAY MENU AND GET USER CHOICE.
        while self.check_1:
            self.view.user_choice()
            answer = input(">> ")
            if answer.upper() in self.menu:
                self.user_choice = self.menu[answer.upper()]
                self.check_1 = False
            else:
                self.view.error_entry()
        return self.user_choice.handler


class RapportTournamentMenuController:
    """
    This controller display all tournament in database. The user can chose it
     with selecting the key of the element.
    """
    def __init__(self):
        self.menu = Menu()
        self.view = MenuView(self.menu)
        self.db = DataBase()
        self.check_1 = True

    def __call__(self):
        self.view.welcome_tournament_rapports()
        for dict_tournament in self.db.tournaments_table:
            self.menu.add(
                "auto", f"    NOM : '{dict_tournament['name']}',"
                        f" LIEU : '{dict_tournament['place']}',"
                        f" DATE DE DEBUT : '{dict_tournament['date_start']}', "
                        f" DATE DE FIN : '{dict_tournament['date_end']}',"
                        f" ROUND(S) JOUÉ(S) :"
                        f" '{len(dict_tournament['all_round'])}' sur"
                        f" '{dict_tournament['nb_total_round']}',"
                        f" NOMBRE DE JOUEURS :"
                        f" '{len(dict_tournament['players_tournament'])}'"
                        f" CONTRÔLE DE TEMPS :"
                        f" '{dict_tournament['control_time']}'.",
                        RapportTournamentController(self.db, dict_tournament))

        self.menu.add("Q", "  Revenir au précédent menu.",
                      HomeMenuController())

        # DISPLAY MENU AND GET USER CHOICE.
        while self.check_1:
            self.view.user_choice()
            answer = input(">> ")
            if answer.upper() in self.menu:
                self.user_choice = self.menu[answer.upper()]
                self.check_1 = False
            else:
                self.view.error_entry()
        return self.user_choice.handler
