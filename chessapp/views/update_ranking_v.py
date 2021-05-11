
class UpdateRankingView:
    """
    All views for UpdateRankingController.
    """

    # WELCOME MESSAGE.
    @staticmethod
    def welcome(instance_player):
        print(f"\nEntrez le nouveau classement général pour :"
              f" '{instance_player.family_name} {instance_player.first_name}',"
              f" né(e) le : '{instance_player.date_of_birth}', classement général actuel :"
              f" '{instance_player.ranking}'. \n")

    # SHOW GLOBAL RANKING FROM DATA BASE.
    @staticmethod
    def show_global_ranking(player_db_sorted):
        print("\n\n VOICI LE CLASSEMENT GÉNÉRAL ACTUEL :\n\n")
        for player in player_db_sorted:
            print(f">'{player.family_name}, {player.first_name}' né(e) le : '{player.date_of_birth}',"
                  f" classement général actuel : '{player.ranking}'.")

    @staticmethod
    def ranking_ok_and_free():
        print(" Cette valeur est libre et est assignée à votre joueur.")

    @staticmethod
    def ranking_ok():
        print(" Cette valeur est assignée à votre joueur.")

    @staticmethod
    def ranking_exists():
        print(f"> INFORMATION : Une joueur de la base de données a déjà cette position dans le classement général.")

    @staticmethod
    def ranking_exists_keep():
        print(f"> Vous voulez quand même sauvegarder ce classement général ?  oui 'O' , non 'N'.")

    @staticmethod
    def error_yes_no():
        print("> INFORMATION :  Ici, oui 'O' ou non 'N' est attendue comme réponse. \n")

    @staticmethod
    def positive_value_needed():
        print("> INFORMATION : Ici un entier positif est attendu.")
