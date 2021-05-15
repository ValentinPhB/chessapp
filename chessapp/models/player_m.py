
class Player:
    """
    Player() instances represents players.
    """

    def __init__(self, family_name=None, first_name=None, date_of_birth=None, gender=None, ranking=None):
        self._family_name = family_name
        self._first_name = first_name
        self._date_of_birth = date_of_birth
        self._gender = gender
        self._ranking = ranking
        self._result = float(0.0)
        self._point = float(0.0)

    def __repr__(self, *args, **kwargs):
        return str(vars(self))

    def __hash__(self):
        return hash((self._family_name, self._first_name, self._date_of_birth, self._gender))

    def __eq__(self, other):
        return ((self._family_name, self._first_name, self._date_of_birth,
                 self._gender) == (other.family_name, other.first_name, other.date_of_birth, other.gender))

    # 1 FAMILY NAME.
    @property
    def family_name(self):
        return self._family_name

    @family_name.setter
    def family_name(self, value):
        self._family_name = value

    # 2 FIRST NAME.
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    # 3 DATE OF BIRTH.
    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        self._date_of_birth = value

    # 4 GENDER.
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    # 5 RANKING.
    @property
    def ranking(self):
        return self._ranking

    @ranking.setter
    def ranking(self, value):
        self._ranking = value

    # 6 RESULT.
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = float(value)

    # 7 POINT.
    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        self._point = value

    def increment_point(self, value):
        self._point += float(value)
