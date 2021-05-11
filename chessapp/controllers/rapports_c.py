# import lib standard sans install

# import lib a installer

# import lib locales
from chessapp.controllers import menus_c


class RapportController:
    """
    NOT IMPLEMENTED YET.
    """
    def __init__(self,):
        pass

    def __call__(self):
        print("CLÉ NON IMPLÉMENTÉE.")
        print("RETOUR MENU HOMME")
        return menus_c.HomeMenuController()

    # • Liste de tous les acteurs :
    #     ◦ par ordre alphabétique ;
    #     ◦ par classement.
    # • Liste de tous les joueurs d'un tournoi :
    #     ◦ par ordre alphabétique ;
    #     ◦ par classement.
    # • Liste de tous les tournois.
    # • Liste de tous les tours d'un tournoi.
    # • Liste de tous les matchs d'un tournoi.
