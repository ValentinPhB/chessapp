from chessapp.utils.constant import DEFAULT_ROUND
from chessapp.model.match import Match


class Tournament:
    """

    """

    def __init__(self, name=None, place=None, date_start=None, date_end=None, nb_total_round=DEFAULT_ROUND,
                 players_tournament=None, control_time=None, description=None):
        self._name = name
        self._place = place
        # a déclancher lors de lé création des rounds
        self._date_start = date_start

        # datetime.datetime.today().strftime('%d-%m-%Y')

        self._date_end = date_end
        self._nb_total_round = nb_total_round
        self.all_round = []
        self._players_tournament = players_tournament
        self._control_time = control_time
        self._description = description

    def __repr__(self, *args, **kwargs):
        return str(vars(self))

    def __hash__(self):
        return hash((self._name, self._place, self._date_start, self._date_end))

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return (self._name, self._place, self._date_start, self._date_end) == (other.name, other.place,
                                                                                   other.date_start, other.date_end)
        return False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value.capitalize()
        else:
            pass

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, value):
        if isinstance(value, str):
            self._place = value.capitalize()
        else:
            pass

    @property
    def date_start(self):
        return self._date_start

    @property
    def date_end(self):
        return self._date_end

    @property
    def nb_total_round(self):
        return self._nb_total_round

    @nb_total_round.setter
    def nb_total_round(self, value):
        if isinstance(value, int) and value < 0:
            self._nb_total_round = value
        else:
            pass

    @property
    def players_tournament(self):
        return self._players_tournament

    @players_tournament.setter
    def players_tournament(self, value):
        self._players_tournament = value

    @property
    def control_time(self):
        return self._control_time

    @control_time.setter
    def control_time(self, value):
        if value.lower() == "bullet" or "blitz" or "coup rapide":
            self._control_time = value.lower()

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if isinstance(value, str):
            self._description = value
        else:
            pass

    def create_first_match(self):
        """
        Description: This method will create matches for the first round in first_round_matches.
        :return: first_round_matches as instance of round for all_rounds (Tournament Instance).
        """
        self.players_tournament.sort(key=lambda x: (- x.point, x.ranking))

        length = len(self._players_tournament)
        middle_index = length // 2
        first_half = self._players_tournament[:middle_index]
        second_half = self._players_tournament[middle_index:]
        i = 0
        list_show_matches = []
        list_with_result = []
        for element in first_half:
            list_with_result.append(Match(player_1=element, result_1=element.result, player_2=second_half[i],
                                          result_2=second_half[i].result))
            list_show_matches.append((element, second_half[i]))
            i += 1
        return list_show_matches, list_with_result

    def create_round_n(self):
        """
        :return:
        """

        self.players_tournament.sort(key=lambda x: (- x.point, x.ranking))

        list_show_matches = []
        list_with_result = []

        i = 0
        while i <= 6:
            a = Match(player_1=self.players_tournament[i], result_1=self.players_tournament[i].result,
                      player_2=self.players_tournament[i+1], result_2=self.players_tournament[i+1].result)
            list_with_result.append(a)
            list_show_matches.append((self.players_tournament[i], self.players_tournament[i+1]))
            i += 2
        return list_show_matches, list_with_result

    def all_points_and_results(self):
        points_max = 0
        for element in self.players_tournament:
            missing = True
            while missing:
                entry = input(f"Combien de points pour ce joueur ? ( 1 , 0.5 , 0 ) {element.first_name} > ")
                try:
                    value = float(entry)
                    if value == 0 and points_max <= 4:
                        element.point += value
                        element.result = value
                        points_max += value
                        missing = False
                    elif value == 0.5 and points_max < 4:
                        element.point += value
                        element.result = value
                        points_max += value
                        missing = False
                    elif value == 1 and points_max < 4:
                        element.point += value
                        element.result = value
                        points_max += value
                        missing = False
                    elif points_max > 4:
                        print("Le total de points possible est dépassé.")
                        points_max = 4
                        # Pour consol, mettre cette fonction dans une while et ici faire un input
                        # ( " Vous voulez continuer ? O / N")
                        # Si O >  return bool pour relancer while + break et la fonction repart

                    else:
                        print("la valeur entrée n'est pas conforme aux attentes ( 1 , 0.5, 0 ).")
                except ValueError:
                    print("Except ValueError")

    def reset_points_and_results(self):
        for element in self.players_tournament:
            element.point = 0
            element.result = 0

    def update_ranking(self):
        for element in self.players_tournament:
            missing = True
            while missing:
                entry = input(f"Quel classement pour ce joueur ? {element.first_name} > ")
                try:
                    value = int(entry)
                    if 0 < value:
                        element.ranking = int(value)
                        missing = False
                    else:
                        print("Ici nous attendons un entier supérieur à 1.")
                except ValueError:
                    print("Ici nous attendons un entier supérieur à 1.")



#     """
    #     :return:
    #     """
    #     pass
    #
    # def continue_tournament(self):
    #     """
    #
    #     :return:
    #     """
    #     pass
    #
    # def show_tournament(self):
    #     """
    #
    #     :return:
    #     """
    #     pass
