from datetime import datetime
from chessapp.utils.constant import DEFAULT_ROUND


class Round:
    number_round = 1
    """

    """
    def __init__(self, nb_total_round=DEFAULT_ROUND):
        self._id = f"ROUND {Round.number_round}"
        self._nb_total_round = nb_total_round
        self._matches_for_round = []
        self._time_starts = (datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        self._time_ends = None
        Round.number_round += 1

    def __repr__(self):
        return str(vars(self))

    def __hash__(self):
        return hash(self._id)

    @property
    def id(self):
        return self._id

    @property
    def nb_total_round(self):
        return self._nb_total_round

    @property
    def matches_for_round(self):
        return self._matches_for_round

    @property
    def time_starts(self):
        return self._time_starts

    @property
    def time_end(self):
        return self._time_ends

    @classmethod
    def reset_nb_round(cls):
        cls.number_round = 1

    def auto_end_time(self):
        self._time_ends = (datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

