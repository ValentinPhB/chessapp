from datetime import datetime
import time

from tinydb import where

from chessapp.models.db_logic_m import DataBase
from chessapp.views.create_tournament_v import CreateTournamentView
from chessapp.controllers import menus_c
from chessapp.utils.constant_u import DEFAULT_ROUND
from chessapp.utils.clear_screen_u import Clear


class CreateTournamentController:
    """
    This controller will collect all information needed to create a tournament.
    (name, place, nb_total_round, date_starts, control_time, description)
    A tournament will be a Tournament() instance.
    Then checking if this new tournament doesn't already exists in database.
    If not, this tournament will be added to the data base.
    """

    def __init__(self, current_tournament):
        self._tournament = current_tournament
        self._view = CreateTournamentView()
        self._players_chosen = []
        self._check_1 = True
        self._check_2 = True
        self._check_3 = True
        self._check_4 = True
        self._db = DataBase()

    def __call__(self):
        # CLEAR SCREEN.
        Clear().screen()

        # FIRST MESSAGE.
        self._view.welcome()

        # CHECKING IF TOURNAMENT ALREADY EXISTS.
        while self._check_4:

            # NAME.
            self._view.user_name_tournament()
            while self._check_1:
                answer = input(">> ")
                test = answer.replace(" ", "")

                if len(answer) == 0 or len(test) == 0:
                    self._view.empty_answer()

                else:
                    self._tournament.name = str(answer.capitalize())
                    self._check_1 = False

            self._check_1 = True

            # CLEAR SCREEN.
            Clear().screen()

            # FIRST MESSAGE.
            self._view.welcome()

            # PLACE.
            self._view.user_place_tournament()

            while self._check_1:
                answer = input(">> ")
                test = answer.replace(" ", "")

                if len(answer) == 0 or len(test) == 0:
                    self._view.empty_answer()

                else:
                    self._tournament.place = str(answer.upper())
                    self._check_1 = False

            self._check_1 = True

            # CLEAR SCREEN.
            Clear().screen()

            # FIRST MESSAGE.
            self._view.welcome()

            # TOTAL NUMBER OF ROUND.
            self._view.user_nb_round_tournament(DEFAULT_ROUND)
            self._view.error_yes_no()

            while self._check_1:
                answer = input(">> ")
                if answer.upper() == 'N':
                    self._check_1 = False
                    self._view.enter_value()

                    while self._check_2:
                        inp_nb_round = input(">> ")
                        try:
                            if int(inp_nb_round) > 0:
                                self._tournament.nb_total_round = str(inp_nb_round)
                                self._check_2 = False

                            else:
                                self._view.positive_value_needed()

                        except ValueError:
                            self._view.positive_value_needed()

                elif answer.upper() == 'O':
                    self._check_1 = False

                else:
                    self._view.error_yes_no()

            self._check_1 = True
            self._check_2 = True

            # CLEAR SCREEN.
            Clear().screen()

            # FIRST MESSAGE.
            self._view.welcome()

            # DATE STARTS.
            self._view.user_date_tournament()
            self._view.error_yes_no()

            while self._check_1:
                answer = input(">> ")
                if answer.upper() == 'O':
                    self._tournament.date_start = datetime.now().date().strftime("%d/%m/%Y")
                    self._check_1 = False

                elif answer.upper() == 'N':

                    day = self._loop_date("DU JOUR", val_max=31, _format="dd")
                    month = self._loop_date("DU MOIS", val_max=12, _format="mm")
                    year = self._loop_date("DE L'ANNÉE", val_max=float("inf"), _format="yyyy", gender="e")

                    # CHECKING IF DATE EXISTS.
                    try:
                        datetime(int(year), int(month), int(day))
                        self._tournament.date_start = f"{day}/{month}/{year}"
                        self._check_1 = False

                    except ValueError:
                        # CLEAR SCREEN.
                        Clear().screen()

                        self._view.wrong_dates()
                        self._check_1 = True
                        self._view.user_date_tournament()
                        self._view.error_yes_no()

                else:
                    self._view.error_yes_no()

            self._check_1 = True

            # CLEAR SCREEN.
            Clear().screen()

            # FIRST MESSAGE.
            self._view.welcome()

            # CONTROL_TIME.
            self._view.user_control_time_ask()
            self._view.control_time_guide()

            while self._check_1:
                inp_control_time = input(">> ")
                try:
                    test = int(inp_control_time)
                    if test == 1:
                        self._tournament.control_time = "bullet"
                        self._check_1 = False

                    elif test == 2:
                        self._tournament.control_time = "blitz"
                        self._check_1 = False

                    elif test == 3:
                        self._tournament.control_time = "coup rapide"
                        self._check_1 = False

                    else:
                        self._view.control_time_guide()

                except ValueError:
                    self._view.control_time_guide()

            self._check_1 = True

            # CLEAR SCREEN.
            Clear().screen()

            # FIRST MESSAGE.
            self._view.welcome()

            # DESCRIPTION.
            self._view.user_description()

            while self._check_1:
                answer = input(">> ")
                test = answer.replace(" ", "")

                if len(answer) == 0:
                    self._view.empty_answer()

                elif len(test) == 0:
                    self._view.empty_answer()

                else:
                    self._tournament.description = str(answer.capitalize())
                    self._check_1 = False

            # CHECKING IF TOURNAMENT ALREADY EXISTS IN DATABASE.
            if self._db.tournaments_table.contains((
                    (where('name') == self._tournament.name) & (
                    where('place') == self._tournament.place) & (
                    where('date_start') == self._tournament.date_start) & (
                    where('nb_total_round') == self._tournament.nb_total_round) & (
                    where('control_time') == self._tournament.control_time) & (
                    where('description') == self._tournament.description))):

                self._view.already_in_db()
                self._view.welcome_already()

            else:
                self._check_4 = False

        # CLEAR SCREEN.
        Clear().screen()

        # SAVING STATE IN DATA BASE.
        self._db.save_tournament(self._tournament)
        self._view.saving_state()
        time.sleep(2)

        return menus_c.AddPlayerMenuController(self._tournament)

    # Optimisation format date_start.
    def _loop_date(self, d_m_y, val_max, _format, gender=""):
        self._check_2 = True
        needed_var = 0
        self._view.loop_date_start_v(d_m_y, gender, _format, val_max)

        while self._check_2:
            inp_d_m_y = input(">> ")
            try:
                if 10 <= int(inp_d_m_y) <= val_max:
                    needed_var = str(inp_d_m_y)
                    self._check_2 = False

                elif 9 >= int(inp_d_m_y) >= 1 == len(inp_d_m_y):
                    needed_var = f"0{str(inp_d_m_y)}"
                    self._check_2 = False

                elif 9 >= int(inp_d_m_y) >= 1 and len(inp_d_m_y) == 2:
                    needed_var = str(inp_d_m_y)
                    self._check_2 = False

                else:
                    self._view.error_loop_date_start(val_max, _format)

            except ValueError:
                self._view.error_loop_date_start(val_max, _format)

        # CLEAR SCREEN.
        Clear().screen()

        return needed_var
