
from chessapp.models.db_logic_m import DataBase


class AddPlayersViews:
    """
    All views for AddNewPlayerController.
    """

    def __init__(self):
        self.db = DataBase()

    # WELCOME MESSAGE.
    @staticmethod
    def welcome():
        print("\n\nAJOUTER UN NOUVEAU JOUEUR À LA BASE DE DONNÉES ET AU TOURNOI.")

    # FAMILY NAME.
    @staticmethod
    def player_family_name():
        print("\n Veuillez entrer le NOM DE FAMILLE du joueur :\n")

    # FIRST NAME.
    @staticmethod
    def player_first_name():
        print("\n Veuillez entrer le PRÉNOM du joueur : \n")

    # DATE OF BIRTH MESSAGE.
    @staticmethod
    def player_date_birth():
        print("\n DATE DE NAISSANCE du joueur :")

    # DAY/MONTH/YEAR DATE OF BIRTH.
    @staticmethod
    def loop_date_birth(d_m_y, gender, _format, val_max):
        print(f"\n Entrez la valeur numérique {d_m_y} souhaité{gender} :")
        print(f" 1 < VOTRE VALEUR {_format} < {val_max}\n")

    # GENDER.
    @staticmethod
    def player_gender_1():
        print("\nGENRE du joueur :")

    @staticmethod
    def player_gender_2():
        print("\n Choisissez Homme '1' ou Femme '2' pour le genre du joueur.\n")

    # RANKING.
    @staticmethod
    def player_ranking_1():
        print("\nCLASSEMENT GÉNÉRAL du joueur :")

    @staticmethod
    def player_ranking_2():
        print("\n\n Quel est le classement général pour ce nouveau joueur ?:")

    # TOOLS TO INTERACT WITH USER.
    @staticmethod
    def welcome_already():
        print(
            "\n\nRÉASSIGNEZ DE NOUVELLES VALEURS AU JOUEUR POUR QU'IL N'AIT AUCUN DOUBLE DANS LA BASE DE DONNÉES.")
        print("Si les conditions sont remplies ce joueur sera ajouté à la base de données et au présent tournoi.")

    @staticmethod
    def error_gender():
        print("> INFORMATION :  Ici, Homme '1' ou Femme '2' est attendue comme réponse. \n")

    @staticmethod
    def positive_value_needed():
        print("> INFORMATION : Ici un entier positif est attendu.")

    @staticmethod
    def special_answer():
        print("> INFORMATION : Ici, une chaine de caratères <lettres sans espaces> est attendue comme réponse. ")
        print("Pour les chaines composées veillez à utiliser la convention d'écriture : 'CamelCase'.")
        print("> exemple : MariePierre\n")

    @staticmethod
    def wrong_dates():
        print("\n Cette date n'existe pas veuillez en entrer une autre.")

    @staticmethod
    def error_loop_date_birth(val_max, _format):
        print(f"> INFORMATION : Ici un entier positif est attendu.")
        print(f" 1 < VOTRE VALEUR {_format} < {val_max}\n")

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
    def no_players_db():
        print("\n> INFORMATION : Il n'y a actuellement aucun joueur dans la base de données.\n")

    def ranking_suggestion(self):
        nb_player_db = len(self.db.players_table)
        print(f"> INFORMATION : Il y a > '{nb_player_db}' < joueurs dans la base de données.")
        print("TAPEZ 'C' POUR AFFICHER LE CLASSEMENT GÉNÉRAL ACTUEL.\n")

    @staticmethod
    def ranking_ok():
        print(" Cette valeur est libre et est assignée à votre joueur.")

    @staticmethod
    def already_in_db():
        print("\n>>> INFORMATION : Il n'y a actuellement un joueur identique dans la base de données.")
        print("Ce joueur n'est donc pas sauvegardé.")
        print("Ce joueur n'est donc pas ajouté au tournoi.")

    # SAVING MESSAGE.
    @staticmethod
    def saving_state():
        print("\n\n\n>> L'ÉTAT ACTUEL DU TOURNOI EST SAUVEGARDÉ DANS LA BASE DE DONNÉES <<\n")

    # SAVING PLAYER MESSAGE.
    @staticmethod
    def saving_player():
        print("\n>>> CE NOUVEAU JOUEUR EST SAUVEGARDÉ DANS LA BASE DE DONNÉES <<<\n")

    # SHOW GLOBAL RANKING FROM DATA BASE.
    @staticmethod
    def show_global_ranking(player_db_sorted):
        print("\n\n VOICI LE CLASSEMENT GÉNÉRAL ACTUEL :\n")
        for player in player_db_sorted:
            print(f">'{player.family_name}, {player.first_name}' né(e) le : '{player.date_of_birth}',"
                  f" classement général actuel : '{player.ranking}'.")
