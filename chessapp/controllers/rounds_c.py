
from chessapp.controllers import menus_c
from chessapp.views.round_v import RoundMakerView
from chessapp.models.match_m import Match
from chessapp.models.round_m import Round
from chessapp.controllers.end_c import EndTournamentController
from chessapp.utils.clear_screen_u import Clear


class RoundMakerController:
    """
    This controller will create matches for rounds in function of the state of
     the current tournament.
    If it's the first round, if the last round has been already payed and for
     all other rounds.
    """

    def __init__(self, current_tournament):
        self.tournament = current_tournament
        self.nb_total_round = self.tournament.nb_total_round
        self.tournament_all_round = current_tournament.all_round
        self.view = RoundMakerView()
        self.round = Round(self.tournament.all_round, self.nb_total_round)
        self.check_1 = True
        self.check_2 = True

    def __call__(self):
        # CLEAR SCREEN.
        Clear().screen()

        # IF IT'S FIRST ROUND.
        if len(self.tournament.all_round) < 1:
            self.view.welcome(self.tournament)

            matches_for_round = self._first_matches()
            self.round.matches = matches_for_round
            self.tournament.add_round(self.round)

            self.view.precedent_matches_message(self.tournament)
            self.view.display_matches(self.tournament)

            return menus_c.RoundMakingMenuController(self.tournament)

        # IF IT'S BETWEEN THE FIRST AND THE LAST ROUND.
        elif 1 <= len(self.tournament.all_round) < int(self.tournament.nb_total_round):

            precedent_round = self.tournament.all_round[-1]
            if precedent_round.matches[0].result_1 == precedent_round.matches[0].result_2 == 0.0:

                # RESULT NON ASSIGNED.
                # SHOW PRECEDENT MATCH AN ASSIGN IT.
                self.view.precedent_matches_message(self.tournament)
                self.view.display_matches(self.tournament)
                return menus_c.RoundMakingMenuController(self.tournament)

            else:

                # RESULT ALREADY ASSIGNED.
                # CREATE NEXT ROUND.
                self.view.welcome(self.tournament)
                matches_for_round = self._matches_n()
                self.round.matches = matches_for_round

                self.tournament.add_round(self.round)
                self.view.display_matches(self.tournament)

                return menus_c.RoundMakingMenuController(self.tournament)

        # IF THE LAST ROUND HAS BEEN PLAYED.
        else:
            return EndTournamentController(self.tournament)

    # SWISS ALGORITHM FOR THE FIRST MATCHES.
    def _first_matches(self):

        self.tournament.players_tournament.sort(key=lambda x: (- x.point, x.ranking))

        length = len(self.tournament.players_tournament)
        middle_index = length // 2

        first_half = self.tournament.players_tournament[:middle_index]
        second_half = self.tournament.players_tournament[middle_index:]

        i = 0
        list_return = []
        for element in first_half:
            list_return.append(Match(player_1=element, result_1=0, player_2=second_half[i],
                                     result_2=0))
            i += 1

        return list_return

    # SWISS ALGORITHM FOR ALL OTHER MATCHES.
    def _matches_n(self):

        players_sorted = sorted(self.tournament.players_tournament, key=lambda x: (- x.point, x.ranking))
        players_remaining = players_sorted[:]
        list_return = []
        list_already_chosen = []

        if len(self.tournament.all_round) % 7 == 0:
            already_done = []
        elif len(self.tournament.all_round) < 7:
            matches_lists = []

            for element in self.tournament.all_round:
                matches_lists.append(element.matches)

            already_done = []
            self.check_1 = True
            i = 0
            while self.check_1:
                try:
                    one_list = matches_lists[i]
                    for element_1 in one_list:
                        already_done.append(element_1)
                    i += 1
                except IndexError:
                    self.check_1 = False
        else:
            i = 1
            while (len(self.tournament.all_round) - i) % 7 != 0:
                i += 1
            list_under_seven_matches = self.tournament.all_round[-i:]
            matches_lists = []

            for element in list_under_seven_matches:
                matches_lists.append(element.matches)

            already_done = []
            self.check_1 = True
            i = 0
            while self.check_1:
                try:
                    one_list = matches_lists[i]
                    for element_1 in one_list:
                        already_done.append(element_1)
                    i += 1
                except IndexError:
                    self.check_1 = False

        for i in range(len(players_sorted)):
            self.check_1 = True
            j = 1
            while self.check_1:
                try:
                    player_1 = players_sorted[i]
                    player_2 = players_sorted[i + j]

                    if player_1 in list_already_chosen:
                        self.check_1 = False
                        continue

                    elif player_1 and player_2 in list_already_chosen:
                        self.check_1 = False
                        continue

                    else:
                        pass

                    while player_2 in list_already_chosen:
                        j += 1
                        try:
                            player_2 = players_sorted[i + j]

                        except IndexError:
                            player_2 = "test"
                            self.check_1 = False
                            continue

                    match = Match(player_1=player_1, result_1=0, player_2=player_2,
                                  result_2=0)

                    match_reversed = Match(player_1=player_2, result_1=0, player_2=player_1,
                                           result_2=0)

                    if match in already_done or match_reversed in already_done:
                        j += 1
                    else:
                        list_already_chosen.append(player_1)
                        list_already_chosen.append(player_2)
                        players_remaining.remove(player_1)
                        players_remaining.remove(player_2)
                        already_done.append(match)
                        list_return.append(match)
                        self.check_1 = False
                except IndexError:
                    self.check_1 = False
                    continue

        if len(list_return) < 4:

            for i in range(len(players_remaining)):
                if i % 2 == 0:
                    player_1 = players_remaining[i]
                    player_2 = players_remaining[i + 1]

                    match = Match(player_1=player_1, result_1=0, player_2=player_2,
                                  result_2=0)
                    list_return.append(match)
                else:
                    continue
        else:
            pass
        return list_return
