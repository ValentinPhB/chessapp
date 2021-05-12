
class RoundMakerView:
    """
    All views for RoundMakerController.
    """

    # WELCOME MESSAGE.
    @staticmethod
    def welcome(current_tournament):
        nb_total_round = current_tournament.nb_total_round
        nb_round = len(current_tournament.all_round) + 1

        print(f"\n\n>>> CRÉATION DU ROUND '{nb_round}' sur '{nb_total_round}' ET DE SES MATCHES. <<<\n")

    # WELCOME MESSAGE 2.
    @staticmethod
    def precedent_matches_message(current_tournament):
        nb_total_round = current_tournament.nb_total_round
        nb_actual_round = len(current_tournament.all_round)
        control_time = current_tournament.control_time

        print(f"VOICI LES MATCHS POUR LE ROUND '{nb_actual_round}' sur '{nb_total_round}' QUE VOUS AVEZ GÉNÉRÉ :")
        print(f"RAPPEL DU CONTRÔLE TIME : '{control_time}'.\n")

    # DISPLAY MATCHES.
    @staticmethod
    def display_matches(current_tournament):
        all_players = current_tournament.players_tournament
        list_matches = current_tournament.all_round[-1].matches

        i = 1
        for element in list_matches:
            print(f"\n> MATCH {i} :"
                  f" '{element.first_p.family_name} {element.first_p.first_name}'"
                  f" né le : '{element.first_p.date_of_birth}'"
                  f" classement du tournoi '{(all_players.index(element.first_p)) + 1}'"
                  f" | CONTRE |"
                  f" '{element.second_p.family_name} {element.second_p.first_name}'"
                  f" né le : '{element.second_p.date_of_birth}'"
                  f" classement du tournoi '{(all_players.index(element.second_p)) + 1}' ")
            i += 1
