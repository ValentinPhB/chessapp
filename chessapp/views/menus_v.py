from chessapp.utils.clear_screen_u import Clear


class MenuView:
    """
    All views for HomeMenuController, AddPlayerMenuController,
     PlayerDataMenuController, ContinueMenuController,
    RoundMakingMenuController, SuggestRankingMenuController and
     UpdateRankingMenuController.
    """

    def __init__(self, menu):
        self.menu = menu

    # DISPLAY MENU.
    def _display_menu(self):
        print("\n\nChoisissez votre option : \n")

        for key, entry in self.menu.items():
            print(f'{key}: {entry}\n')

    # FUNCTION FOR REDIRECTING USER.
    def user_choice(self):
        self._display_menu()

    # WELCOME MESSAGE HOME CONTROLLER.
    @staticmethod
    def welcome_home():
        print("\nCENTRE ÉCHECS\n")
        print("\nAccueil du gestionnaire de tournoi.")

    # WELCOME MESSAGE ADD PLAYERS.
    @staticmethod
    def welcome_add_player(nbr_player_add):
        print("\n\n\nAJOUTEZ DES JOUEURS.")
        print(f"Il vous reste > '{8 - nbr_player_add}' < à ajouter.")

    # WELCOME MESSAGE CONTINUE TOURNAMENT.
    @staticmethod
    def welcome_continue():
        print("\n\nCONTINUER UN TOURNOI.")

    # WELCOME MESSAGE REPORT MENU.
    @staticmethod
    def welcome_reports():
        print("\n\nCHOISISSEZ L'OBJET POUR LEQUEL VOUS SOUHAITEZ DES INFORMATIONS.")

    # WELCOME TOURNAMENT REPORT MENU.
    @staticmethod
    def welcome_tournament_reports():
        print("\n\nCHOISISSEZ LE TOURNOIS POUR LEQUEL VOUS SOUHAITEZ DES INFORMATIONS.")

    # WELCOME MESSAGE ADD PLAYER FROM DATA.
    @staticmethod
    def welcome_add_from_data():
        print("\n\nAJOUTER UN NOUVEAU JOUEUR AU TOURNOI DEPUIS LA BASE DE DONNÉES.")

    # WELCOME MESSAGE UPDATE GLOBAL RANKING.
    @staticmethod
    def welcome_update_global_ranking():
        print("\n\n\nMODIFIEZ LE CLASSEMENT D'UN JOUEUR :")

    # SAVING MESSAGE.
    @staticmethod
    def saving_state():
        print("\n\n\n\n>> L'ÉTAT ACTUEL DU TOURNOI EST SAUVEGARDÉ DANS LA BASE DE DONNÉES <<\n")

    # SHOW RANKING TOURNAMENT.
    @staticmethod
    def show_ranking_tournament(players_tournament):
        # CLEAR SCREEN.
        Clear().screen()

        players_tournament.sort(key=lambda x: (- x.point, x.ranking))
        print(">> VOICI LE CLASSEMENT POUR CE TOURNOI :\n\n")
        i = 1

        for player in players_tournament:
            print(f"PLACE N°{i} : '{player.family_name}, {player.first_name}'"
                  f" né(e) le : '{player.date_of_birth}',"
                  f" classement général actuel : '{player.ranking}',"
                  f" total de points pour ce tournoi : '{player.point}'.")
            i += 1

    # TOOLS TO INTERACT WITH USER
    @staticmethod
    def no_players_db():
        print("\n> INFORMATION : Il n'y a actuellement aucun joueur dans la base de données "
              "que vous pourriez ajouter.")
        print("> Tout joueur déjà ajouté à ce présent tournoi ne peut être affiché.")
        print("> Choisissez la clé '2' pour créer un nouveau joueur et l'enregistrer dans la base de données.")

    @staticmethod
    def error_entry():
        print("> INFORMATION : Ici vous devez choisir une des clés proposées.\n")

    @staticmethod
    def no_tournament_db():
        print("\n> INFORMATION : Il n'y a actuellement aucun tournoi non-terminé dans la base de données.")
        print("> Vous êtes redirigé sur le menu d'accueil.\n")

    @staticmethod
    def repeat_nbr_remaining(nbr_player_add):
        print(f"\nIl vous reste {8 - nbr_player_add} à ajouter.\n")

    @staticmethod
    def none_data():
        print("\n> INFORMATION : Il n'y a actuellement aucune information dans la base de données.")
        print("> Vous êtes redirigé sur le menu d'accueil.\n")
