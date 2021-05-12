
class CreateTournamentView:
    """
    All views for CreateTournamentController.
    """

    # WELCOME MESSAGE.
    @staticmethod
    def welcome():
        print("CRÉER UN TOURNOI.")

    # NAME.
    @staticmethod
    def user_name_tournament():
        print("\n Quel NOM voulez-vous donner au tournoi ? \n")

    # PLACE.
    @staticmethod
    def user_place_tournament():
        print("\n Quel LIEU voulez-vous affilier au tournoi ? \n")

    # TOTAL NUMBER OF ROUND.
    @staticmethod
    def user_nb_round_tournament(default_round):
        print(f"\n Le NOMBRE DE TOUR est-il ÉGAL à la valeur par défault suivante > {default_round} < ?")

    # DATE START.
    @staticmethod
    def user_date_tournament():
        print("\n Le tournoi commence-t'il en DATE DU PRÉSENT JOUR ?")

    # CONTROL TIME.
    @staticmethod
    def user_control_time_ask():
        print("\n Quel CONTRÔLE DE TEMPS pour ce tournoi ?")

    # DESCRIPTION.
    @staticmethod
    def user_description():
        print("\n Quelle DESCRIPTION voulez-vous affilier à ce tournoi ? \n")

    # TOOLS TO INTERACT WITH USER.
    @staticmethod
    def already_in_db():
        print("\n> INFORMATION : Il n'y a actuellement un tournoi identique dans la base de données.\n")
        print("Ce tournoi ne peut être créé.")

    @staticmethod
    def welcome_already():
        print("\n\nRÉASSIGNEZ DE NOUVELLES VALEURS AU TOURNOI POUR QU'IL N'AIT AUCUN DOUBLE DANS LA BASE DE DONNÉES.")
        print("Si les conditions sont remplies ce tournoi sera créé.")

    @staticmethod
    def error_yes_no():
        print("> INFORMATION :  Ici, oui 'O' ou non 'N' est attendue comme réponse. \n")

    @staticmethod
    def enter_value():
        print(" \n Entrez votre valeur pour le nombre de rounds souhaité : \n ")

    @staticmethod
    def positive_value_needed():
        print("> INFORMATION : Ici un entier positif est attendu.")

    @staticmethod
    def control_time_guide():
        print("> INFORMATION : Ici ;  bullet '1' , blitz '2' ou coup rapide '3' est attendue comme réponse. \n")

    @staticmethod
    def empty_answer():
        print("> INFORMATION : Ici, une chaine de caratère est attendue comme réponse. \n ")

    @staticmethod
    def wrong_dates():
        print("\nCette date n'existe pas veuillez en entrer une autre.")

    @staticmethod
    def loop_date_start_v(d_m_y, gender, _format, val_max):
        print(f"\nVeuillez entrer la valeur numérique {d_m_y} souhaité{gender} :")
        print(f" 1 < VOTRE VALEUR {_format} < {val_max}\n")

    @staticmethod
    def error_loop_date_start(val_max, _format):
        print(f"> INFORMATION : Ici un entier positif est attendu. 1 < VOTRE VALEUR {_format} < {val_max}\n")

    @staticmethod
    def save_or_correct_v(entry):
        print(f"> INFORMATION : Voulez-vous SAUVEGARDER 'S' ou CORRIGER 'C' l'entrée : '{entry}' ?\n")

    # SAVING MESSAGE.
    @staticmethod
    def saving_state():
        print("\n\n\n\n>> L'ÉTAT ACTUEL DU TOURNOI EST SAUVEGARDÉ DANS LA BASE DE DONNÉES <<\n")
