
class EndScreenView:
    """
    All views for EndScreenController, EndScreenSaveController and EndTournamentController.
    """

    # SAVING MESSAGE.
    @staticmethod
    def saving_state():
        print("\n\n\n\n>> L'ÉTAT ACTUEL DU TOURNOI EST SAUVEGARDÉ DANS LA BASE DE DONNÉES <<")

    # QUIT.
    @staticmethod
    def quit():
        print("\n> Vous quittez l'application.\n")

    # SHOW RANKING TOURNAMENT.
    @staticmethod
    def show_ranking_tournament(player_tournament_sorted):
        print("--------------------------------------------------------"
              "-------------------------------------------------------\n")
        print("\n\nLE NOMBRE DE ROUNDS POUR CE TOURNOI À ÉTÉ ATTEINT ET"
              " LES RÉSULTATS DES PRÉCÉDENTS MATCHS ONT ÉTÉ ASSIGNÉS.")
        print(">> VOICI LE CLASSEMENT POUR CE TOURNOI :\n\n")
        i = 1
        for player in player_tournament_sorted:
            print(f"PLACE N°{i} : '{player.family_name}, {player.first_name}' né(e) le : '{player.date_of_birth}',"
                  f" classement général actuel : '{player.ranking}', total de points pour ce tournoi :"
                  f" '{player.point}'.")
            i += 1

    # SHOW GLOBAL RANKING FROM DATA BASE.
    @staticmethod
    def show_global_ranking(player_db_sorted):
        print("\n\n\n>> MISE À JOUR DU CLASSEMENT GÉNÉRAL POUR CHAQUE JOUEUR DE LA BASE DE DONNÉES.")
        print(" CLASSEMENT GÉNÉRAL ACTUEL :\n\n")
        for player in player_db_sorted:
            print(f">'{player.family_name}, {player.first_name}' né(e) le : '{player.date_of_birth}',"
                  f" classement général actuel : '{player.ranking}'.")

    # WELCOME ASSIGNATION MESSAGE.
    @staticmethod
    def welcome_assignation_ranking():
        print("\n\nVEUILLEZ RÉASSIGNER DES VALEURS POUR CHAQUE JOUEUR DE LA BASE DE DONNÉES"
              " ET AINSI METTRE À JOUR LE CLASSEMENT GÉNÉRAL:")

    # CHOOSE RANKING.
    @staticmethod
    def choose_ranking_message(player):
        print(f"\nQuel classement pour :  '{player['family_name']}, {player['first_name']}',"
              f" né(e) le : '{player['date_of_birth']}' >?<")

    # RANKING ALREADY EXISTS
    @staticmethod
    def ranking_exists():
        print(f"> INFORMATION : Une joueur de la base de données a déjà cette position dans le classement général.\n")

    # TOOLS TO INTERACT WITH USER.
    @staticmethod
    def positive_value_needed():
        print("> INFORMATION : Ici un entier positif est attendu.")

    @staticmethod
    def ranking_ok():
        print(" Cette valeur est libre et est assignée à votre joueur.")

    @staticmethod
    def error_yes_no():
        print("> INFORMATION :  Ici, oui 'O' ou non 'N' est attendue comme réponse. \n")

    @staticmethod
    def ranking_exists_keep():
        print(f"> Vous voulez quand même sauvegarder ce classement général?  oui 'O' , non 'N'.")
