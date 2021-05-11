
from chessapp.controllers import menus_c
from chessapp.views.round_v import RoundMakerView
from chessapp.models.match_m import Match
from chessapp.models.round_m import Round
from chessapp.controllers.end_c import EndTournamentController


class RoundMakerController:
    """
    This controller will create matches for rounds in function of the state of the current tournament.
    If it's the first round, if the last round has been already payed and for all other rounds.
    """

    def __init__(self, current_tournament):
        self.tournament = current_tournament
        self.nb_total_round = self.tournament.nb_total_round
        self.tournament_all_round = current_tournament.all_round
        self.view = RoundMakerView()
        self.round = Round(self.tournament.all_round, self.nb_total_round)

    def __call__(self):

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
            list_return.append(Match(player_1=element, result_1=element.result, player_2=second_half[i],
                                     result_2=second_half[i].result))
            i += 1
        return list_return

    # SWISS ALGORITHM FOR ALL OTHER MATCHES ||||||| IN PROCESS ||||||||||.
    def _matches_n(self):

        self.tournament.players_tournament.sort(key=lambda x: (- x.point, x.ranking))
        i = 0
        list_return = []
        while i <= 6:
            list_return.append((Match(player_1=self.tournament.players_tournament[i],
                                      result_1=self.tournament.players_tournament[i].result,
                                      player_2=self.tournament.players_tournament[i + 1],
                                      result_2=self.tournament.players_tournament[i + 1].result)))
            i += 2
        return list_return
