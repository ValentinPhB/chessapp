
class Match:
    """
    Match() instances represents matches between two players.
    Match() instances will be contained in Round() instances themselves contained in Tournament() instance.
    """

    def __init__(self, player_1=None, result_1=None, player_2=None, result_2=None):
        self._match = ([player_1, result_1], [player_2, result_2])

        self._first_p = player_1
        self._second_p = player_2
        self._result_1 = result_1
        self._result_2 = result_2

    def __repr__(self, *args, **kwargs):
        return str(vars(self))

    def __hash__(self):
        return hash((self._first_p, self._second_p))

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return (self._first_p, self._second_p) == (other.first_p, other.second_p)

    @property
    def first_p(self):
        return self._first_p

    @first_p.setter
    def first_p(self, value):
        self._first_p = value

    @property
    def second_p(self):
        return self._second_p

    @second_p.setter
    def second_p(self, value):
        self._second_p = value

    @property
    def result_1(self):
        return self._result_1

    @result_1.setter
    def result_1(self, value):
        self._result_1 = value

    @property
    def result_2(self):
        return self._result_2

    @result_2.setter
    def result_2(self, value):
        self._result_2 = value

    @property
    def match(self):
        return self._match

    @match.setter
    def match(self, value):
        self._match = value
