from tinydb import TinyDB

from models.player import Player
from models.round import Round
from models.match import Match


class Tournament:
    class Decorators(object):
        @classmethod
        def to_db(cls, func):
            def save_into_db(*args, **kwargs):
                func(*args, **kwargs)
                serialized_tournament = [
                    tournament.serialize()
                    for tournament in Tournament.TOURNAMENT
                ]
                db = TinyDB('db.json')
                tournaments_table = db.table('tournaments')
                tournaments_table.truncate()
                tournaments_table.insert_multiple(serialized_tournament)

            return save_into_db

    TOURNAMENT = []

    def __init__(self, name, place, date,
                 time_control, description, rounds_total=4):
        self.name = name
        self.place = place
        self.date = date
        self.rounds_total = int(rounds_total)
        self.rounds = []
        self.players = []
        self.time_control = time_control
        self.description = description

    @classmethod
    @Decorators.to_db
    def add_tournament(cls, tournament):
        cls.TOURNAMENT.append(tournament)

    @classmethod
    def get_tournament(cls, index):
        return cls.TOURNAMENT[index]

    @Decorators.to_db
    def add_player(self, player_id):
        self.players.append([player_id, 0])  # second argument is the score

    @property
    def player_count(self):
        return len(self.players)

    def get_suisse_sorted_players(self):
        s = sorted(
            self.players,
            key=lambda player: int(Player.get_player(player[0]).rank),
            reverse=True
        )  # sort by rank
        return sorted(
            s,
            key=lambda player: float(player[1]),
            reverse=True
        )  # then sort by score

    def create_round(self):
        round_name = 'Round' + str(len(self.rounds) + 1)
        round = Round(round_name)
        self.rounds.append(round)
        return round

    @Decorators.to_db
    def generate_matches(self):
        matches = []
        round = self.create_round()
        players = self.get_suisse_sorted_players()
        print(players)
        if len(self.rounds) == 1:
            for i in range(self.rounds_total):
                match = Match(players[i][0], players[i + self.rounds_total][0])
                matches.append(match)
        else:
            while len(players) > 1:
                y = 1
                while self.played_against(players[0][0], players[y][0]):
                    y += 1
                match = Match(players[0][0], players[y][0])
                matches.append(match)
                del players[y]
                del players[0]
        round.add_matches(matches)

    def played_against(self, player_one, player_two):
        opposition = []
        for round in self.rounds:
            for match in round.matches:
                opposition.append([match.result[0][0], match.result[1][0]])

        return [player_one, player_two] in opposition \
            or [player_two, player_one] in opposition

    @Decorators.to_db
    def update_players_score(self):
        for player in self.players:
            score = 0
            for round in self.rounds:
                for match in round.matches:
                    if player[0] == match.result[0][0]:
                        score += match.result[0][1]
                    if player[0] == match.result[1][0]:
                        score += match.result[1][1]
            player[1] = score

    def get_players(self):
        return [player[0] for player in self.players]

    def get_players_by_score(self):
        return sorted(
            self.players,
            key=lambda player: float(player[1]),
            reverse=True
        )

    def get_players_by_rank(self):
        return sorted(
            self.get_players(),
            key=lambda player: int(Player.get_player(player).rank),
            reverse=True
        )

    def get_players_by_alpha(self):
        return sorted(
            self.get_players(),
            key=lambda player: Player.get_player(player).name
        )

    @Decorators.to_db
    def close_last_round(self):
        self.rounds[-1].close()

    def finished(self):
        if len(self.rounds) < self.rounds_total:
            return False
        return all(round.is_closed() for round in self.rounds)

    def serialize(self):
        return {
            'name': self.name,
            'place': self.place,
            'date': self.date,
            'rounds_total': self.rounds_total,
            'rounds': [round.serialize() for round in self.rounds],
            'players': self.players,
            'time_control': self.time_control,
            'description': self.description,
        }

    @classmethod
    def deserialize(cls, serialized_tournament):
        name = serialized_tournament['name']
        place = serialized_tournament['place']
        date = serialized_tournament['date']
        time_control = serialized_tournament['time_control']
        description = serialized_tournament['description']
        rounds_total = serialized_tournament['rounds_total']
        tournament = Tournament(name, place, date, time_control,
                                description, rounds_total)
        tournament.rounds = [
            Round.deserialize(serialized_round)
            for serialized_round in serialized_tournament['rounds']
        ]
        tournament.players = serialized_tournament['players']

        return tournament

    @classmethod
    def load_all_from_db(cls):
        cls.TOURNAMENT = []
        db = TinyDB('db.json')
        tournaments_table = db.table('tournaments')
        serialized_tournaments = tournaments_table.all()
        for serialized_tournament in serialized_tournaments:
            tournament = Tournament.deserialize(serialized_tournament)
            Tournament.add_tournament(tournament)

    def to_report(self):
        return {
            'name': self.name,
            'place': self.place,
            'date': self.date,
            'total_players': self.player_count,
            'time_control': self.time_control,
            'description': self.description,
            'rounds_total': self.rounds_total,
            'finished': self.finished()
        }
