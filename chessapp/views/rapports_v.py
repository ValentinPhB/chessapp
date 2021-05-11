
class RapportPlayerViews:
    """
    All views for RapportPlayerController.
    """

    # WELCOME MESSAGE.
    @staticmethod
    def welcome():
        print("\n\nLISTE DE TOUS LES ACTEURS :\n")

    # DISPLAY ACTORS IN ALPHABETIC ORDER.
    @staticmethod
    def display_actors_rank(players_table):
        print("\nPAR ORDRE ALPHABÉTIQUE :\n")
        sorted_list = sorted(players_table,
                             key=lambda k: int(k['family_name']))
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
        print("LES DEUX RAPPORTS CONCERNANT LES JOUEURS ENREGISTRÉS DANS LA"
              " BASE DE DONNÉES SONT AFFICHÉS CI-DESSUS.")
        print("> INFORMATION : Vous êtes redirigé vers le menu de rapports.")


class RapportTournamentViews:
    """
    All views for RapportTournamentController.
    """
    def __init__(self, dict_tournament):
        self.dict_tournament = dict_tournament

    # WELCOME MESSAGE.
    @staticmethod
    def welcome():
        print("\n\nINFORMATIONS CONCERNANT LE TOURNOI CHOISI :\n")

    def all_player_tournament(self):
        print("VOICI TOUS LES JOUEURS DU TOURNOI CHOISI :")
        print("> Par ordre alphabétique :\n")
        player_tournament = self.dict_tournament['players_tournament']
        player_tournament_alpha = sorted(player_tournament,
                                         key=lambda k: k['family_name'])
        for player in player_tournament_alpha:
            print(f"    NOM DE FAMILLE : '{player['family_name']}',"
                  f" PRÉNOM : '{player['first_name']}',"
                  f" DATE DE NAISSANCE : '{player['date_of_birth']}', "
                  f"SEXE : '{player['gender']}'")
        print("\n> Par ordre du classement du tournoi :\n")
        player_tournament_rank = sorted(player_tournament,
                                        key=lambda k: (- float(k['point']),
                                                       int(k['ranking'])))
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
            print(f"\n>> >> >> POUR LE '{_round['name']}' sur"
                  f" '{_round['nb_total_round']}',"
                  f" DÉBUT : '{_round['time_starts']}',"
                  f" FIN : '{_round['time_ends']}'<< << << \n")
            list_matches = _round['matches']
            print("VOICI LES MATCHS POUR CE ROUND :")
            i = 1
            for _matches in list_matches:
                print(f"\n>>> MATCH '{i}' :")
                print(f"JOUEUR 1 : '{_matches['first_p']['family_name']}' ,"
                      f" '{_matches['first_p']['first_name']}',"
                      f" né(e) le : '{_matches['first_p']['date_of_birth']},"
                      f" classement général :"
                      f" '{_matches['first_p']['ranking']},"
                      f" point(s) total :"
                      f" '{_matches['first_p']['point']}',"
                      f" |CONTRE|"
                      f" JOUEUR 2 : '{_matches['second_p']['family_name']}' ,"
                      f" '{_matches['second_p']['first_name']}',"
                      f" né(e) le : '{_matches['second_p']['date_of_birth']},"
                      f" classement général :"
                      f" '{_matches['second_p']['ranking']},"
                      f" total de points pour ce tournoi :"
                      f" '{_matches['second_p']['point']}',")
                print("\n> RÉSULTATS POUR CE MATCH :")
                print(f"JOUEUR 1 : '{_matches['result_1']}'"
                      f" point(s) pour ce match. ||"
                      f" JOUEUR 2 : '{_matches['result_2']}'"
                      f" point(s) pour ce match.\n")
                i += 1
                self._stop()

    @staticmethod
    def finish():
        print("LES RAPPORTS CONCERNANT LE TOURNOI CHOISI SONT AFFICHÉS"
              " CI-DESSUS.")
        print("> INFORMATION : Vous êtes redirigé vers le menu de rapports.\n")

    @staticmethod
    def _stop():
        print("\n---------------------------------------------------------"
              "--------------------------------")
        print("|Le prompt suivant marque un temps d'arrêt pour faciliter "
              "votre lecture des informations|")
        _pass = input("|         Entrez n'importe quel caractère pour"
                      " continuer, ou appuyez sur entrée         |")
        print("---------------------------------------------------------"
              "-------------------------------\n")
        return _pass
