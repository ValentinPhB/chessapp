from model.tournament import Tournament
from model.player import Player
from model.round import Round

# import à changer pour fichier contenant all actors.
from chessapp.utils.constant import list_of_all_players


def main():
    # étape 1 faire un tournois et lui assigner 8 joueurs.
    # creation de tournement sans affectation param
    current_tournament = Tournament()

    # ou reprise d'un ancien tournois
    # current_tournament = REPRISE

    # creation joueurs et affectation param
    # ne pas oublier choix possible dans joueurs déja enregistrés

    # i = 1
    # players_for_tournament =[]
    # while i <= 8:
    #     b = input("family_name >")
    #     c = input("first_name >")
    #     d = input("date of birth >" )
    #     e = input("gender >")
    #     f = int(input("ranking >"))
    #
    #     # rajouter current_tournament la BDD all players
    #     list_of_all_players.append(Player(b, c, d, e, f))
    #
    #     # rajouter au tournois
    #     players_for_tournament.append(Player(b, c, d, e, f))
    #     i += 1
    #

    # liste de huit faux joueurs :
    b = Player("Pheulpin", "Valentin", "24/06/93", "f", 1)
    c = Player("JEAN", "Clara", "20/11/96", "m", 2)
    d = Player("Borde", "antoine", "21/05/93", "f", 5)
    e = Player("Pompougnac", "louis", "13/11/93", "m", 8)
    f = Player("Pistre", "Natasha", "01/01/93", "f", 3)
    g = Player("JAUMARD", "Julie", "02/02/93", "f", 4)
    h = Player("BELLANGER", "Antoine", "04/04/90", "m", 6)
    j = Player("Huitre", "URsul", "04/06/80", "m", 7)
    players_for_tournament = [b, c, d, e, f, g, h, j]

    # affectation param liste d'instance de joueurs
    current_tournament.players_tournament = players_for_tournament

    # Création de l'instance Round 1
    r_x = Round()

    # Affichage des Matches à jouer
    print(f"Voici les matches du Round {Round.number_round - 1} ")
    print(current_tournament.create_first_match()[0])

    # Mise à jour des résultats post matches :
    current_tournament.all_points_and_results()

    # Mise à jour time_end du round correspondant :
    r_x.auto_end_time()

    # Ajout des instances matches ([player_1, résultat_1] , [player_2, résultat_2]) a l'instance Round correspondante
    r_x.matches_for_round.append(current_tournament.create_first_match()[1])

    # Ajout de l'instance round a l'instance du tournois
    current_tournament.all_round.append(r_x)

    # Vérification
    print(current_tournament.all_round)

    # création des N rounds suivants
    while Round.number_round <= current_tournament.nb_total_round:

        r_x = Round()
        print(f"Voici les matches du Round {Round.number_round - 1} ")
        print(current_tournament.create_round_n()[0])
        current_tournament.all_points_and_results()

        r_x.matches_for_round.append(current_tournament.create_round_n()[1])
        r_x.auto_end_time()
        current_tournament.all_round.append(r_x)

        # vérification
        print("liste de tous les Rounds")
        print(current_tournament.all_round)

    # Simulation affichage du calssement de fin
    print("les classement est : ")
    current_tournament.players_tournament.sort(key=lambda x: (- x.point, x.ranking))
    for element in current_tournament.players_tournament:
        print(f"{element.first_name}, {element.family_name}, {element.date_of_birth}, {element.point}")

    # Mise à jour du classement pas utilisateur
    current_tournament.update_ranking()

    # vérification
    print("UPDATE RANKING")
    for element in current_tournament.players_tournament:
        print(f"{element.first_name}, {element.family_name}, {element.date_of_birth}, {element.ranking}")

    # Reset de result et point pour tous les participants :
    current_tournament.reset_points_and_results()
    # vérification
    print("RESET POINTS AND RESULTS")
    for element in current_tournament.players_tournament:
        print(f"{element.first_name}, {element.family_name}, {element.date_of_birth}, {element.result}, "
              f"{element.point}")

    # Reset Round pour prochain tournois.
    Round.reset_nb_round()
    # Vérification
    print("RESET ROUND")
    print(Round.number_round)

    # remplacer dans liste all joueurs.


if __name__ == "__main__":
    main()
