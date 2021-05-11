
from datetime import datetime


class Round:

    """
    Round() instances represents rounds itself contained in Tournament() instance. It will contains Match() instances.
    """

    def __init__(self, current_tournament_all_round, nb_total_round):
        self.nb_total_round_tournament = len(current_tournament_all_round)
        self._next_round = self.nb_total_round_tournament + 1
        self._name = str(f"ROUND {self._next_round}")
        self._nb_total_round = nb_total_round
        self._matches = None
        self._time_starts = (datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        self._time_ends = None

    def __repr__(self):
        return str(vars(self))

    def __hash__(self):
        return hash(self._name)

    # 1 NAME.
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # 2 NUMBER TOTAL OF ROUND.
    @property
    def nb_total_round(self):
        return self._nb_total_round

    @nb_total_round.setter
    def nb_total_round(self, value):
        self._nb_total_round = value

    # 3 MATCHES.
    @property
    def matches(self):
        return self._matches

    @matches.setter
    def matches(self, value):
        self._matches = value

    # 4 TIME STARTS.
    @property
    def time_starts(self):
        return self._time_starts

    @time_starts.setter
    def time_starts(self, value):
        self._time_starts = value

    # 5 TIME ENDS.
    @property
    def time_ends(self):
        return self._time_ends

    @time_ends.setter
    def time_ends(self, value):
        self._time_ends = value
