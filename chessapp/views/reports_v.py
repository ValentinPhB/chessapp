from chessapp.utils.clear_screen_u import Clear


class ReportPlayerViews:
    """
    All views for RepportPlayerController.
    """

    # WELCOME MESSAGE.
    @staticmethod
    def welcome():
        print("\n\nLISTE DE TOUS LES ACTEURS :\n")

    # DISPLAY ACTORS IN ALPHABETIC ORDER.
    @staticmethod
    def display_actors_rank(players_table):
        print("\nPAR ORDRE ALPHABÉTIQUE :\n")

        sorted_list = sorted(players_table, key=lambda k: k['family_name'])

        for player in sorted_list:
            print(f"    NOM DE FAMILLE : '{player['family_name']}',"
                  f" PRÉNOM : '{player['first_name']}',"
                  f" DATE DE NAISSANCE : '{player['date_of_birth']}',"
                  f" SEXE : '{player['gender']}',"
                  f" CLASSEMENT GÉNÉRAL : '{player['ranking']}'.")

    # DISPLAY ACTORS IN RANKING ORDER.
    @staticmethod
    def display_actors_alpha(players_table):
        print("\nPAR ORDRE AU CLASSEMENT GÉNÉRAL :\n")

        sorted_list = sorted(players_table, key=lambda k: k['ranking'])

        for player in sorted_list:
            print(f"    NOM DE FAMILLE : '{player['family_name']}',"
                  f" PRÉNOM : '{player['first_name']}',"
                  f" DATE DE NAISSANCE : '{player['date_of_birth']}',"
                  f" SEXE : '{player['gender']}',"
                  f" CLASSEMENT GÉNÉRAL : '{player['ranking']}'.")

        print("\n")

    @staticmethod
    def finish():
        print("LES DEUX RAPPORTS CONCERNANT LES JOUEURS ENREGISTRÉS DANS LA BASE DE DONNÉES SONT AFFICHÉS CI-DESSUS.")
        print("> INFORMATION : Vous êtes redirigé vers le menu de rapports.")

    @staticmethod
    def stop_up():
        print("\n-----------------------------------------------------------------------------------------")
        print("|Le prompt suivant marque un temps d'arrêt pour faciliter votre lecture des informations|")

    @staticmethod
    def stop_end():
        print("----------------------------------------------------------------------------------------\n")


class ReportTournamentViews:
    """
    All views for ReportTournamentController.
    """
    def __init__(self, dict_tournament):
        self.dict_tournament = dict_tournament

    # WELCOME MESSAGE.
    @staticmethod
    def welcome(dict_tournament):
        print("\n\nINFORMATIONS CONCERNANT LE TOURNOI CHOISI :\n")
        print(f"NOM : '{dict_tournament['name']}',"
              f" LIEU : '{dict_tournament['place']}',"
              f" DATE DE DEBUT : '{dict_tournament['date_start']}',"
              f" DATE DE FIN : '{dict_tournament['date_end']}',"
              f" ROUND(S) JOUÉ(S) : '{len(dict_tournament['all_round'])}' sur"
              f" '{dict_tournament['nb_total_round']}',"
              f" NOMBRE DE JOUEURS : '{len(dict_tournament['players_tournament'])}'"
              f" CONTRÔLE DE TEMPS :'{dict_tournament['control_time']}'.\n")

    def all_player_tournament(self):
        print("VOICI TOUS LES JOUEURS DU TOURNOI CHOISI :")
        print("> Par ordre alphabétique :\n")

        player_tournament = self.dict_tournament['players_tournament']
        player_tournament_alpha = sorted(player_tournament, key=lambda k: k['family_name'])

        for player in player_tournament_alpha:
            print(f"    NOM DE FAMILLE : '{player['family_name']}',"
                  f" PRÉNOM : '{player['first_name']}',"
                  f" DATE DE NAISSANCE : '{player['date_of_birth']}', "
                  f"SEXE : '{player['gender']}'")

        print("\n> Par ordre du classement du tournoi :\n")

        player_tournament_rank = sorted(player_tournament, key=lambda k: (- k['point'], k['ranking']))
        i = 1
        for player in player_tournament_rank:
            print(f"PLACE N°{i} :"
                  f"   NOM DE FAMILLE : '{player['family_name']}',"
                  f" PRÉNOM : '{player['first_name']}',"
                  f" DATE DE NAISSANCE : '{player['date_of_birth']}',"
                  f" SEXE : '{player['gender']}',"
                  f" CLASSEMENT GÉNÉRAL : '{player['ranking']}'.")
            i += 1

        self._stop()

    def all_rounds_tournament(self):
        print("\nLISTE DE TOUS LES TOUR DU TOURNOI CHOISI :")

        list_rounds = self.dict_tournament['all_round']

        for _round in list_rounds:
            # CLEAR SCREEN.
            Clear().screen()
            print(f"\n>> >> >> POUR LE '{_round['name']}' sur '{_round['nb_total_round']}',"
                  f" DÉBUT : '{_round['time_starts']}',"
                  f" FIN : '{_round['time_ends']}' << << << \n")

            list_matches = _round['matches']
            print("\nVOICI LES MATCHS POUR CE ROUND :")
            i = 1

            for _matches in list_matches:
                print(f"\n>>> MATCH '{i}' :")

                print(f"JOUEUR 1 : '{_matches['first_p']['family_name']}' ,'{_matches['first_p']['first_name']}',"
                      f" né(e) le : '{_matches['first_p']['date_of_birth']},"
                      f" classement général : '{_matches['first_p']['ranking']},"
                      f" point(s) total : '{_matches['first_p']['point']}',"
                      f" |CONTRE|"
                      f" JOUEUR 2 : '{_matches['second_p']['family_name']}' , '{_matches['second_p']['first_name']}',"
                      f" né(e) le : '{_matches['second_p']['date_of_birth']},"
                      f" classement général :'{_matches['second_p']['ranking']},"
                      f" total de points pour ce tournoi : '{_matches['second_p']['point']}',")

                print("\n> RÉSULTATS POUR CE MATCH :")

                print(f"JOUEUR 1 : '{_matches['result_1']}' point(s) pour ce match. ||"
                      f" JOUEUR 2 : '{_matches['result_2']}' point(s) pour ce match.\n")
                i += 1

                self._stop()

    @staticmethod
    def finish():
        print("LES RAPPORTS CONCERNANT LE TOURNOI CHOISI SONT AFFICHÉS CI-DESSUS.")
        print("> INFORMATION : Vous êtes redirigé vers le menu de rapports.\n")

    @staticmethod
    def _stop():
        print("\n\n\n-----------------------------------------------------------------------------------------")
        print("|Le prompt suivant marque un temps d'arrêt pour faciliter votre lecture des informations|")
        _pass = input("|         Entrez n'importe quel caractère pour continuer, ou appuyez sur entrée         |")
        print("----------------------------------------------------------------------------------------\n\n")
        return _pass
