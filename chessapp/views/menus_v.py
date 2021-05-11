
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

    # WELCOME MESSAGE RAPPORT MENU.
    @staticmethod
    def welcome_rapports():
        print("\n\nCHOISISSEZ L'OBJET POUR LEQUEL VOUS SOUHAITEZ"
              " DES INFORMATIONS.")

    # WELCOME TOURNAMENT RAPPORT MENU.
    @staticmethod
    def welcome_tournament_rapports():
        print("\n\nCHOISISSEZ LE TOURNOIS POUR LEQUEL VOUS SOUHAITEZ"
              " DES INFORMATIONS.")

    # WELCOME MESSAGE ADD PLAYER FROM DATA.
    @staticmethod
    def welcome_add_from_data():
        print("\n\nAJOUTER UN NOUVEAU JOUEUR AU TOURNOI DEPUIS LA"
              " BASE DE DONNÉES.")

    # WELCOME MESSAGE UPDATE GLOBAL RANKING.
    @staticmethod
    def welcome_update_global_ranking():
        print("\n\n\nMODIFIEZ LE CLASSEMENT D'UN JOUEUR :")

    # TOOLS TO INTERACT WITH USER
    @staticmethod
    def no_players_db():
        print("\n> INFORMATION : Il n'y a actuellement aucun joueur"
              " dans la base de données que vous pourriez ajouter.")
        print("> Tout joueur déjà ajouté à ce présent tournoi ne peut"
              " être affiché.")
        print("> Choisissez la clé '1' pour créer un nouveau joueur et"
              " l'enregistrer dans la base de données.")

    @staticmethod
    def error_entry():
        print("> INFORMATION : Ici vous devez choisir une des clés"
              " proposées.\n")

    @staticmethod
    def no_tournament_db():
        print("\n> INFORMATION : Il n'y a actuellement aucun tournoi"
              " non-terminé dans la base de données.")
        print("> Vous êtes redirigé sur le menu d'accueil.\n")

    @staticmethod
    def repeat_nbr_remaining(nbr_player_add):
        print(f"\nIl vous reste {8 - nbr_player_add} à ajouter.\n")

    @staticmethod
    def none_data():
        print("\n> INFORMATION : Il n'y a actuellement aucune information"
              " dans la base de données.")
        print("> Vous êtes redirigé sur le menu d'accueil.\n")
