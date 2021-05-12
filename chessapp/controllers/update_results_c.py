import time
from datetime import datetime

from chessapp.views.update_results_v import UpdateResultsView
from chessapp.controllers import menus_c
from chessapp.models.db_logic_m import DataBase
from chessapp.utils.clear_screen_u import Clear


class UpdateResultsController:
    """
    The user enter points for all players after a match.
    This controller will checking if points all distributed properly.
    """

    def __init__(self, current_tournament):
        self.tournament = current_tournament
        self.round = self.tournament.all_round[-1]
        self.matches = self.round.matches
        self.view = UpdateResultsView()
        self.check_1 = True
        self.db = DataBase()

    def __call__(self):
        # CLEAR SCREEN.
        Clear().screen()

        # RESET ALL RESULTS FOR NEW MATCHES.
        for element in self.tournament.players_tournament:
            element.result = float(0.0)

        self.view.welcome()
        self.view.information_message()
        self.view.information_value()

        for element in self.matches:
            self.check_1 = True
            while self.check_1:
                total_answer = 0
                self.view.show_match(element)
                self.view.show_player(element.first_p)
                answer_1 = self._checking_value()
                total_answer += answer_1

                self.view.show_player(element.second_p)
                answer_2 = self._checking_value()
                total_answer += answer_2
                if total_answer == 1:

                    # ASSIGN RESULT player 1.
                    element.first_p.result = float(answer_1)
                    element.result_1 = float(answer_1)

                    # INCREMENT POINTS PLAYER 1 FOR TOURNAMENT RANKING.
                    element.first_p.increment_point(answer_1)

                    # ASSIGN RESULT player 2.
                    element.second_p.result = float(answer_2)
                    element.result_2 = float(answer_2)

                    # INCREMENT POINTS PLAYER 1 FOR TOURNAMENT RANKING.
                    element.second_p.increment_point(answer_2)
                    self.check_1 = False

                else:
                    self.view.error_max_point()
                    self.view.information_value()

        # SET DATE_ENDS FOR ROUND.
        self.tournament.all_round[-1].time_ends = (datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        self.view.auto_add_ends()
        time.sleep(2)

        # SAVE ACTUAL STATE.
        self.db.save_tournament(self.tournament)
        self.view.saving_state()

        # RETURN FOR SUGGEST UPDATE RANKING.
        return menus_c.SuggestRankingMenuController(self.tournament)

    # TOOL FOR CHECKING VALUE.
    def _checking_value(self):
        check_2 = True
        test = None
        while check_2:
            answer = input(">> ")
            try:
                test = float(answer)

                if test == 1:
                    check_2 = False

                elif test == 0:
                    check_2 = False

                elif test == 0.5:
                    check_2 = False

                else:
                    self.view.error_entry()

            except ValueError:
                self.view.error_entry()

        return test
