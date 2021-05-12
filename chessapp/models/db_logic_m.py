
from tinydb import TinyDB, where

from chessapp.models.match_m import Match
from chessapp.models.player_m import Player
from chessapp.models.round_m import Round
from chessapp.models.tournament_m import Tournament


class DataBase:
    """
    This class contains all methods in charge of data persistence for
     Tournament() and Player() (save and retrieve).
    """

    def __init__(self):
        # INITIALIZATION/OPEN 'db_centre_echec.json'
        # DATA BASE AND CREATE TABLES.
        self.db = TinyDB('db_centre_echec.json')
        self.tournaments_table = self.db.table('tournaments')
        self.players_table = self.db.table('players')

    @staticmethod
    def serialize_tournament(tournament):
        # SERIALIZE A TOURNAMENT.
        # FROM INSTANCES TO TINYDB TOURNAMENTS TABLE.
        instances_rounds = tournament.all_round
        instances_players = tournament.players_tournament

        dicts_rounds = []
        dicts_players = []

        for player in instances_players:
            a = {"family_name": player.family_name, "first_name": player.first_name,
                 "date_of_birth": player.date_of_birth, "gender": player.gender, "ranking": player.ranking,
                 "result": player.result, "point": player.point}

            dicts_players.append(a)

        for round_x in instances_rounds:
            matches_list = []

            name = round_x.name
            nb_total_round = round_x.nb_total_round
            time_starts = round_x.time_starts
            time_ends = round_x.time_ends

            instances_matches = round_x.matches
            for match in instances_matches:

                first_p = match.first_p
                second_p = match.second_p

                serialized_first_p = {"family_name": first_p.family_name,
                                      "first_name": first_p.first_name,
                                      "date_of_birth": first_p.date_of_birth,
                                      "gender": first_p.gender,
                                      "ranking": first_p.ranking,
                                      "result": first_p.result,
                                      "point": first_p.point}

                serialized_second_p = {"family_name": second_p.family_name,
                                       "first_name": second_p.first_name,
                                       "date_of_birth": first_p.date_of_birth,
                                       "gender": second_p.gender,
                                       "ranking": second_p.ranking,
                                       "result": second_p.result,
                                       "point": second_p.point}

                result_1 = match.result_1
                result_2 = match.result_2

                serialized_match = ([serialized_first_p, result_1], [serialized_second_p, result_2])

                b = {"match": serialized_match, "first_p": serialized_first_p, "second_p": serialized_second_p,
                     "result_1": result_1, "result_2": result_2}

                matches_list.append(b)

            c = {"name": name, "nb_total_round": nb_total_round, "matches": matches_list, "time_starts": time_starts,
                 "time_ends": time_ends}

            dicts_rounds.append(c)

        return {"name": tournament.name, "place": tournament.place,
                "date_start": tournament.date_start,
                "date_end": tournament.date_end,
                "nb_total_round": tournament.nb_total_round,
                "all_round": dicts_rounds,
                "players_tournament": dicts_players,
                "control_time": tournament.control_time,
                "description": tournament.description}

    def save_tournament(self, tournament):
        # SAVING TOURNAMENT() IN TINY DATA BASE.
        # CHECKING IF IT ALREADY EXISTS IN DATA BASE.
        if self.tournaments_table.contains((where("name") == tournament.name) & (
                where("place") == tournament.place) & (
                where("date_start") == tournament.date_start) & (
                where("description") == tournament.description)):

            serialize_tournament = self.serialize_tournament(tournament)

            self.tournaments_table.remove((where("name") == tournament.name) & (
                where("place") == tournament.place) & (
                where("date_start") == tournament.date_start))

            self.tournaments_table.insert(serialize_tournament)

        else:
            serialize_tournament = self.serialize_tournament(tournament)
            self.tournaments_table.insert(serialize_tournament)

    @staticmethod
    def retrieve_tournament(tournament):
        # RETRIEVE A TOURNAMENT FROM TINYDB DATABASE.
        # FROM 'DICT' TO INSTANCES.
        continue_tournament = Tournament()

        continue_tournament.name = tournament["name"]
        continue_tournament.place = tournament["place"]
        continue_tournament.date_start = tournament["date_start"]
        continue_tournament.date_end = tournament["date_end"]
        continue_tournament.nb_total_round = tournament["nb_total_round"]
        continue_tournament.control_time = tournament["control_time"]
        continue_tournament.description = tournament["description"]

        all_rounds = []

        dict_rounds_list = tournament["all_round"]

        for element_1 in dict_rounds_list:
            round_instance = Round(tournament['all_round'], tournament['nb_total_round'])
            round_instance.name = element_1["name"]
            round_instance.time_starts = element_1["time_starts"]
            round_instance.time_ends = element_1["time_ends"]
            dict_list_matches = element_1["matches"]

            matches_list = []
            for element_2 in dict_list_matches:
                match_instance = Match()

                # FIRST_P DICT TO INSTANCE.
                match_instance.first_p = Player()

                match_instance.first_p.family_name = element_2["first_p"]['family_name']

                match_instance.first_p.first_name = element_2["first_p"]['first_name']

                match_instance.first_p.date_of_birth = element_2["first_p"]['date_of_birth']

                match_instance.first_p.gender = element_2["first_p"]['gender']
                match_instance.first_p.ranking = element_2["first_p"]['ranking']
                match_instance.first_p.result = element_2["first_p"]['result']
                match_instance.first_p.point = element_2["first_p"]['point']

                # SECOND_P DICT TO INSTANCE.
                match_instance.second_p = Player()
                match_instance.second_p.family_name = element_2["second_p"]['family_name']

                match_instance.second_p.first_name = element_2["second_p"]['first_name']

                match_instance.second_p.date_of_birth = element_2["second_p"]['date_of_birth']

                match_instance.second_p.gender = element_2["second_p"]['gender']

                match_instance.second_p.ranking = element_2["second_p"]['ranking']

                match_instance.second_p.result = element_2["second_p"]['result']

                match_instance.second_p.point = element_2["second_p"]['point']

                # RESULTS.
                match_instance.result_1 = element_2["result_1"]
                match_instance.result_2 = element_2["result_2"]

                # MATCH ATTRIBUTE FOR MATCH INSTANCE.
                match_instance.match = ([match_instance.first_p, match_instance.result_1],
                                        [match_instance.second_p, match_instance.result_2])

                # LIST OF ALL MATCHES FOR A ROUND.
                matches_list.append(match_instance)

            # ROUND INSTANCE MATCHES ATTRIBUTES.
            round_instance.matches = matches_list

            # ALL ROUND TOURNAMENT ATTRIBUTES.
            all_rounds.append(round_instance)
        continue_tournament.all_round = all_rounds

        list_dict_players_tournament = tournament['players_tournament']
        players_tournament = []
        for element_3 in list_dict_players_tournament:

            # PLAYER DICT TO PLAYER INSTANCE.
            player_instance = Player()
            player_instance.family_name = element_3["family_name"]
            player_instance.first_name = element_3["first_name"]
            player_instance.date_of_birth = element_3["date_of_birth"]
            player_instance.gender = element_3["gender"]
            player_instance.ranking = element_3["ranking"]
            player_instance.result = element_3["result"]
            player_instance.point = element_3["point"]
            players_tournament.append(player_instance)
        continue_tournament.players_tournament = players_tournament
        return continue_tournament

    @staticmethod
    def serialize_player(player):
        # SERIALIZE PLAYER.
        # FROM INSTANCES TO TINYDB PLAYERS TABLE.
        serialize_player = {"family_name": player.family_name,
                            "first_name": player.first_name,
                            "date_of_birth": player.date_of_birth,
                            "gender": player.gender, "ranking": player.ranking,
                            "result": player.result, "point": player.point}
        return serialize_player

    def save_player(self, player):
        # SAVING PLAYER() IN TINY DATA BASE.
        # CHECKING IF IT ALREADY EXISTS IN DATA BASE.
        if self.players_table.search(
                (where("family_name") == player.family_name) & (
                    where("first_name") == player.first_name) & (
                    where("date_of_birth") == player.date_of_birth)):

            serialize_player = self.serialize_player(player)
            self.players_table.remove(
                (where("family_name") == player.family_name) & (
                    where("first_name") == player.first_name) & (
                    where("date_of_birth") == player.date_of_birth))

            self.players_table.insert(serialize_player)
        else:
            serialize_player = self.serialize_player(player)
            self.players_table.insert(serialize_player)

    @staticmethod
    def retrieve_player(player_json):
        # RETRIEVE A TOURNAMENT FROM TINY DATA BASE.
        # FROM 'DICT' TO INSTANCES.

        player = Player()
        player.family_name = player_json["family_name"]
        player.first_name = player_json["first_name"]
        player.date_of_birth = player_json["date_of_birth"]
        player.gender = player_json["gender"]
        player.ranking = player_json["ranking"]
        player.result = player_json["result"]
        player.point = player_json["point"]
        return player
