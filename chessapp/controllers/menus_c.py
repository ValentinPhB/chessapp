import time

from tinydb import where

from chessapp.utils.menus_u import Menu
from chessapp.views.menus_v import MenuView
from chessapp.controllers.create_tournament_c import CreateTournamentController
from chessapp.controllers.update_ranking_c import UpdateRankingController
from chessapp.controllers.continue_c import ContinueTournamentController
from chessapp.controllers.reports_c import ReportPlayerController, ReportTournamentController
from chessapp.controllers.end_c import EndScreenController, EndScreenSaveController, EndTournamentController
from chessapp.controllers.add_new_players_c import AddNewPlayerController, AddPlayerFromDataController
from chessapp.controllers.rounds_c import RoundMakerController
from chessapp.controllers.update_results_c import UpdateResultsController
from chessapp.models.db_logic_m import DataBase
from chessapp.models.tournament_m import Tournament
from chessapp.utils.clear_screen_u import Clear


class HomeMenuController:
    """
    This controller display the home menu.
     The user can create a new tournament or continue ones not finished.
     The user can also display reports, or quit the application.
    """

    def __init__(self):
        self._menu = Menu()
        self._view = MenuView(self._menu)
        self._user_choice = None
        self._check_1 = True
        self._tournament = Tournament()
        self._db = DataBase()

    def __call__(self):
        # CLEAR SCREEN.
        Clear().screen()

        # ADD MENUS.
        # IF A TOURNAMENT IN DATA BASE IS NOT FINISHED.
        if self._db.tournaments_table.contains(where('date_end') == str("None")):
            self._menu.add("auto", "Continuer le précédent tournoi non-terminé.",
                           ContinueMenuController(self._tournament))

            self._menu.add("auto", "Afficher des rapports.", ReportMenuController())
            self._menu.add("Q", "Quitter l'application.", EndScreenController())

        else:
            self._menu.add("auto", "Créer un tournoi.", CreateTournamentController(self._tournament))
            self._menu.add("auto", "Afficher des rapports.", ReportMenuController())
            self._menu.add("Q", "Quitter l'application.", EndScreenController())

        # DISPLAY MENU AND GET USER CHOICE.
        self._view.welcome_home()

        while self._check_1:
            self._view.user_choice()
            answer = input(">> ")

            if answer.upper() in self._menu:
                self._user_choice = self._menu[answer.upper()]
                self._check_1 = False

            else:
                self._view.error_entry()

        return self._user_choice.handler


class AddPlayerMenuController:
    """
    This controller will display choices for the user.
     The user can create a new player or retrieve it from the data base.
    """

    def __init__(self, current_tournament):
        self._menu = Menu()
        self._view = MenuView(self._menu)
        self._user_choice = None
        self._check_1 = True
        self._tournament = current_tournament

    def __call__(self):
        # CLEAR SCREEN.
        Clear().screen()

        # ADD MENUS.
        self._menu.add("auto", "Choisir un joueur dans la base de données.",
                       PlayerDataMenuController(self._tournament))

        self._menu.add("auto", "Ajouter un nouveau joueur au tournoi et dans la base de données.",
                       AddNewPlayerController(self._tournament))

        self._menu.add("Q", "Sauvegarder et quitter l'application.", EndScreenSaveController(self._tournament))

        # CHECKING IF NUMBER PLAYER < 8 TO REDIRECT PROPERLY.
        players_list = self._tournament.players_tournament
        counting = len(players_list)
        if counting < 8:
            self._view.welcome_add_player(counting)

            while self._check_1:
                self._view.user_choice()
                answer = input(">> ")
                if answer.upper() in self._menu:
                    self._user_choice = self._menu[answer.upper()]
                    self._check_1 = False

                else:
                    self._view.error_entry()
                    self._view.repeat_nbr_remaining(counting)

            return self._user_choice.handler

        else:
            return RoundMakerController(self._tournament)


class PlayerDataMenuController:
    """
    This controller will display all players in data base
     if there are not already chosen in the current tournament.
     The user can chose a player to add it to the tournament.
    """

    def __init__(self, current_tournament):
        self._menu = Menu()
        self._view = MenuView(self._menu)
        self._user_choice = None
        self._check_1 = True
        self._tournament = current_tournament
        self._db = DataBase()

    def __call__(self):
        # CLEAR SCREEN.
        Clear().screen()

        # SELECTING PLAYERS FROM DATA AND SHOW ONLY THOSE
        # WHO ARE NOT ALREADY CHOSEN.
        # ADDING EVERY PLAYER AS MENUS.
        number_player = self._db.players_table.all()
        if len(number_player) >= 1:
            player_to_show = sorted(number_player, key=lambda k: k['ranking'])

            if len(self._tournament.players_tournament) > 0:
                for player_instance in self._tournament.players_tournament:

                    family_name = player_instance.family_name
                    first_name = player_instance.first_name
                    date_of_birth = player_instance.date_of_birth
                    ranking = player_instance.ranking

                    if self._db.players_table.contains((where('family_name') == family_name) & (
                            where('first_name') == first_name) & (
                            where('date_of_birth') == date_of_birth) & (
                            where('ranking') == ranking)):

                        player_to_show[:] = [
                            x for x in player_to_show if not (
                                (x.get('family_name') == family_name) & (
                                    x.get('first_name') == first_name) & (
                                    x.get('date_of_birth') == date_of_birth) & (
                                    x.get('ranking') == ranking))]

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
                    self._menu.add("auto", f"    NOM DE FAMILLE : '{players['family_name']}',"
                                           f" PRÉNOM : '{players['first_name']}',"
                                           f" DATE DE NAISSANCE : '{players['date_of_birth']}',"
                                           f" CLASSEMENT GÉNÉRAL : '{players['ranking']}'.",

                                   AddPlayerFromDataController(self._tournament, players))

                self._menu.add("\nQ", "  REVENIR AU MENU D'AJOUT DES JOUEURS.",
                               AddPlayerMenuController(self._tournament))

                self._view.welcome_add_from_data()

                while self._check_1:
                    self._view.user_choice()
                    answer = input(">> ")
                    if answer.upper() in self._menu:
                        self._user_choice = self._menu[answer.upper()]
                        self._check_1 = False

                    else:
                        self._view.error_entry()

                return self._user_choice.handler

            else:
                self._view.no_players_db()
                time.sleep(3)
                return AddPlayerMenuController(self._tournament)

        else:
            self._view.no_players_db()
            time.sleep(3)
            return AddPlayerMenuController(self._tournament)


class ContinueMenuController:
    """
    This controller will display unfinished tournament.
    """

    def __init__(self, current_tournament):
        self._menu = Menu()
        self._view = MenuView(self._menu)
        self._user_choice = None
        self._check_1 = True
        self._db = DataBase()
        self._tournament = current_tournament

    def __call__(self):
        # CLEAR SCREEN.
        Clear().screen()

        # CHECKING IF THERE'S ONE TOURNAMENT UNFINISHED IN DATA BASE.
        # IN THAT CASE IT WILL DISPLAY IT.
        # OTHERWISE IT WILL INFORM THE USER AND REDIRECT IT TO
        # 'HOME MENU CONTROLLER'.
        if len(self._db.tournaments_table) >= 1:
            for _dict in self._db.tournaments_table:
                if _dict['date_end'] == "None":
                    self._menu.add("auto", f"    NOM : '{_dict['name']}',"
                                   f" LIEU : '{_dict['place']}',"
                                   f" DATE DE DEBUT :"f" '{_dict['date_start']}',"
                                   f"ROUND(S) JOUÉ(S) : '{len(_dict['all_round'])}' sur '{_dict['nb_total_round']}',"
                                   f" NOMBRE DE JOUEURS : '{len(_dict['players_tournament'])}'"
                                   f" CONTRÔLE DE TEMPS : '{_dict['control_time']}'.",
                                   ContinueTournamentController(_dict))

                else:
                    pass

            self._menu.add("Q", "QUITTER ET REVENIR AU MENU D'ACCUEIL.", HomeMenuController())

            self._view.welcome_continue()

            while self._check_1:
                self._view.user_choice()
                answer = input(">> ")
                if answer.upper() in self._menu:
                    self._user_choice = self._menu[answer.upper()]
                    self._check_1 = False

                else:
                    self._view.error_entry()

            return self._user_choice.handler

        else:
            self._view.no_tournament_db()
            time.sleep(3)
            return HomeMenuController()


class RoundMakingMenuController:
    """
    This controller ask the user if he wants to continue or save an quit.
    """

    def __init__(self, current_tournament):
        self._menu = Menu()
        self._view = MenuView(self._menu)
        self._user_choice = None
        self._check_1 = True
        self._tournament = current_tournament
        self._db = DataBase()

    def __call__(self):
        # SAVING STATE.
        self._db.save_tournament(self._tournament)
        self._view.saving_state()

        # ADD MENUS.
        self._menu.add("auto", "Assigner des résultats aux matchs générés.", UpdateResultsController(self._tournament))
        self._menu.add("*", "Afficher le classement actuel du tournoi.", None)
        self._menu.add("Q", "Sauvegarder et quitter l'application.", EndScreenSaveController(self._tournament))

        # DISPLAY MENU AND GET USER CHOICE.
        while self._check_1:
            self._view.user_choice()
            answer = input(">> ")

            if answer.upper() in self._menu and answer.upper() != '*':
                self._user_choice = self._menu[answer.upper()]
                self._check_1 = False
            elif answer == '*':
                self._view.show_ranking_tournament(self._tournament.players_tournament)
                return RoundMakingMenuController(self._tournament)

            else:
                self._view.error_entry()

        return self._user_choice.handler


class SuggestRankingMenuController:
    """
    This controller ask if the user wants to update player's ranking, continue
     the tournament or save and quit.
    """

    def __init__(self, current_tournament):
        self._menu = Menu()
        self._view = MenuView(self._menu)
        self._user_choice = None
        self._tournament = current_tournament
        self._check_1 = True

    def __call__(self):
        # CLEAR SCREEN.
        Clear().screen()

        # ADD MENUS.
        precedent_round = self._tournament.all_round[-1]
        if precedent_round.matches[0].result_1 == precedent_round.matches[0].result_2 == 0.0:
            return RoundMakerController(self._tournament)

        elif int(self._tournament.nb_total_round) == len(self._tournament.all_round) and (
                precedent_round.matches[0].result_1 != precedent_round.matches[0].
                result_2 or precedent_round.matches[0].result_1 == precedent_round.matches[0].result_2 == 0.5):

            return EndTournamentController(self._tournament)

        else:
            self._menu.add("auto", "Générer les prochains matchs.", RoundMakerController(self._tournament))
            self._menu.add("auto", "Changer le classement d'un joueur.", UpdateRankingMenuController(self._tournament))
            self._menu.add("Q", "Sauvegarder et quitter l'application.", EndScreenSaveController(self._tournament))

        # DISPLAY MENU AND GET USER CHOICE.
        while self._check_1:
            self._view.user_choice()
            answer = input(">> ")

            if answer.upper() in self._menu:
                self._user_choice = self._menu[answer.upper()]
                self._check_1 = False

            else:
                self._view.error_entry()

        return self._user_choice.handler


class UpdateRankingMenuController:
    """
    This controller will show every players from the current tournament.
     the user will chose witch one he wants to update the global ranking.
    """

    def __init__(self, current_tournament):
        self._menu = Menu()
        self._db = DataBase()
        self._view = MenuView(self._menu)
        self._user_choice = None
        self._tournament = current_tournament
        self._check_1 = True

    def __call__(self):
        # CLEAR SCREEN.
        Clear().screen()

        # WELCOME MESSAGE.
        self._view.welcome_update_global_ranking()

        # ADD MENUS.
        list_player_db = []
        for player in self._db.players_table:
            instance_player = self._db.retrieve_player(player)
            list_player_db.append(instance_player)

        list_player_db.sort(key=lambda x: int(x.ranking))

        for player_instance in list_player_db:
            self._menu.add("auto", f"'{player_instance.family_name} {player_instance.first_name}',"
                           f" né(e) le : '{player_instance.date_of_birth}',"
                           f" classement actuel : '{player_instance.ranking}'.",
                           UpdateRankingController(self._tournament, player_instance))

        self._menu.add("Q", "Revenir au précédent menu.", SuggestRankingMenuController(self._tournament))

        # DISPLAY MENU AND GET USER CHOICE.
        while self._check_1:
            self._view.user_choice()
            answer = input(">> ")

            if answer.upper() in self._menu:
                self._user_choice = self._menu[answer.upper()]
                self._check_1 = False

            else:
                self._view.error_entry()

        return self._user_choice.handler


class ReportMenuController:
    """
    This controller asks the user to know witch reports he wants.
    """
    def __init__(self):
        self._menu = Menu()
        self._view = MenuView(self._menu)
        self._user_choice = None
        self._db = DataBase()
        self._check_1 = True

    def __call__(self):
        # CLEAR SCREEN.
        Clear().screen()

        # NO PLAYERS AND TOURNAMENT IN DATA.
        if len(self._db.players_table) == len(self._db.tournaments_table) == 0:
            self._view.none_data()
            time.sleep(3)
            return HomeMenuController()

        else:
            self._view.welcome_reports()

            self._menu.add("auto", "Joueurs enregistrés dans la base de données.", ReportPlayerController(self._db))
            self._menu.add("auto", "Tournois enregistrés dans la base de données.", ReportTournamentMenuController())
            self._menu.add("Q", "Revenir au précédent menu.", HomeMenuController())

        # DISPLAY MENU AND GET USER CHOICE.
        while self._check_1:
            self._view.user_choice()
            answer = input(">> ")

            if answer.upper() in self._menu:
                self._user_choice = self._menu[answer.upper()]
                self._check_1 = False

            else:
                self._view.error_entry()

        return self._user_choice.handler


class ReportTournamentMenuController:
    """
    This controller display all tournament in database. The user can chose it
     with selecting the key of the element.
    """
    def __init__(self):
        self._menu = Menu()
        self._view = MenuView(self._menu)
        self._user_choice = None
        self._db = DataBase()
        self._check_1 = True

    def __call__(self):
        # CLEAR SCREEN.
        Clear().screen()

        self._view.welcome_tournament_reports()

        for dict_tournament in self._db.tournaments_table:
            self._menu.add("auto", f"    NOM : '{dict_tournament['name']}',"
                           f" LIEU : '{dict_tournament['place']}',"
                           f" DATE DE DEBUT : '{dict_tournament['date_start']}', "
                           f" DATE DE FIN : '{dict_tournament['date_end']}',"
                           f" ROUND(S) JOUÉ(S) : '{len(dict_tournament['all_round'])}' sur"
                                   f" '{dict_tournament['nb_total_round']}',"
                           f" NOMBRE DE JOUEURS : '{len(dict_tournament['players_tournament'])}'"
                           f" CONTRÔLE DE TEMPS :'{dict_tournament['control_time']}'.",
                           ReportTournamentController(self._db, dict_tournament))

        self._menu.add("Q", "  Revenir au précédent menu.", ReportMenuController())

        # DISPLAY MENU AND GET USER CHOICE.
        while self._check_1:
            self._view.user_choice()
            answer = input(">> ")

            if answer.upper() in self._menu:
                self._user_choice = self._menu[answer.upper()]
                self._check_1 = False

            else:
                self._view.error_entry()
        return self._user_choice.handler
