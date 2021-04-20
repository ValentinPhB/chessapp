class Match:
    """

    """
    def __init__(self, player_1=None, result_1=None, player_2=None, result_2=None):
        self._match = ([player_1, result_1], [player_2, result_2])
        self._first_1 = player_1
        self._second_2 = player_2

    def __repr__(self, *args, **kwargs):
        return str(self._match)

    def __hash__(self):
        return hash((self._first_1, self._second_2))

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return (self._first_1, self._second_2) == (other.first_1, other.second_2)

    @property
    def first_1(self):
        return self._first_1

    @property
    def second_2(self):
        return self._second_2

    @property
    def match(self):
        return self._match
