
class UpdateResultsView:
    """
    All views for UpdateResultsController.
    """

    # WELCOME MESSAGE.
    @staticmethod
    def welcome():
        print("\n\nENTREZ LES RÉSULTATS POUR CHAQUE JOUEUR : \n")

    # INFORMATION VALUE.
    @staticmethod
    def information_message():
        print("> INFORMATION : Ici, pour chaque match la valeur attendue est :")

    @staticmethod
    def information_value():
        print("  1    < pour le gagnant,")
        print("  0,5  < pour les deux joueurs si c'est un match nul,")
        print("  0    < pour le perdant.")

    # SHOW MATCH.
    @staticmethod
    def show_match(instance_match):
        print(f"\n\n\nPOUR LE MATCH OPPOSANT :"
              f" '{instance_match.first_p.family_name} {instance_match.first_p.first_name}'"
              f" né(e) le : {instance_match.first_p.date_of_birth}"
              f" et"
              f" '{instance_match.second_p.family_name} {instance_match.second_p.first_name}'"
              f" né(e) le : {instance_match.second_p.date_of_birth} :\n")

    # SHOW PLAYER.
    @staticmethod
    def show_player(match_player):
        print(f" Attribuez une valeur pour : '{match_player.family_name} {match_player.first_name}'"
              f" né(e) le : {match_player.date_of_birth} :")

    # AUTO ADD TIME ENDS ROUNDS.
    @staticmethod
    def auto_add_ends():
        print("\n> INFORMATION : La temps de fin de round a automatiquement été ajoutée.\n")

    # TOOLS TO INTERACT WITH USER.
    @staticmethod
    def error_entry():
        print(">\n INFORMATION : Ici, '1' ou '0' ou '0.5' est attendue comme réponse.")

    @staticmethod
    def error_max_point():
        print("> INFORMATION : Le nombre de points distribués pour ce match est supérieur ' 1 '. \n")
        print(" Veuillez réassigner les points pour ce match.")

    # SAVING MESSAGE.
    @staticmethod
    def saving_state():
        print("\n\n\n\n>> L'ÉTAT ACTUEL DU TOURNOI EST SAUVEGARDÉ DANS LA BASE DE DONNÉES <<")
