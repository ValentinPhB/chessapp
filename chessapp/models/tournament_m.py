
from chessapp.utils.constant_u import DEFAULT_ROUND


class Tournament:
    """
    Tournament() instance contains all information of the tournament.
     Players() instances, Round() instance, Match() instances.
    """

    def __init__(self, name=None, place=None, date_start=None, nb_total_round=DEFAULT_ROUND, control_time=None,
                 description=None):
        self._name = name
        self._place = place
        self._date_start = date_start
        self._date_end = "None"
        self._nb_total_round = nb_total_round
        self._all_round = []
        self._players_tournament = []
        self._control_time = control_time
        self._description = description

    def __repr__(self, *args, **kwargs):
        return str(vars(self))

    def __hash__(self):
        return hash((self._name, self._place, self._date_start, self._date_end))

    # 1 NAME.
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # 2 PLACE.
    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, value):
        self._place = value

    # 3 DATE START.
    @property
    def date_start(self):
        return self._date_start

    @date_start.setter
    def date_start(self, value):
        self._date_start = value

    # 4 DATE END.
    @property
    def date_end(self):
        return self._date_end

    @date_end.setter
    def date_end(self, value):
        self._date_end = value

    # 5 NUMBER TOTAL ROUND.
    @property
    def nb_total_round(self):
        return self._nb_total_round

    @nb_total_round.setter
    def nb_total_round(self, value):
        self._nb_total_round = value

    # 6 ALL ROUND.
    @property
    def all_round(self):
        return self._all_round

    @all_round.setter
    def all_round(self, value):
        self._all_round = value

    # 7 PLAYERS TOURNAMENT
    @property
    def players_tournament(self):
        return self._players_tournament

    @players_tournament.setter
    def players_tournament(self, value):
        self._players_tournament = value

    # 8 CONTROL TIME.
    @property
    def control_time(self):
        return self._control_time

    @control_time.setter
    def control_time(self, value):
        self._control_time = value

    # 9 DESCRIPTION.
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    # 10 MATCHES ALREADY.
    @property
    def matches_already(self):
        return self._matches_already

    @matches_already.setter
    def matches_already(self, value):
        self._name = value

    # ADD MATCHES IN SELF._MATCHES_ALREADY
    def add_matches_already(self, new):
        self._matches_already.append(new)

    # RESET MATCHES IN SELF._MATCHES_ALREADY
    def reset_matches_already(self):
        self._matches_already = []

    # ADD PLAYER TO SELF._PLAYERS_TOURNAMENT
    def add_player(self, new):
        self._players_tournament.append(new)

    # ADD ROUND TO SELF._ROUND
    def add_round(self, new):
        self._all_round.append(new)
