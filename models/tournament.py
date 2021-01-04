import nums_from_string

from models.player import Player
from models.round import Round
from models.match import Match


class Tournament:

    def __init__(self, name, place, date, rounds_number=4):
        self.name = name
        self.place = place
        self.date = date
        self.rounds_total = int(rounds_number)
        self.rounds = []
        self.players = []
        self.time_control = "bullet"
        self.description = ""
        self.rounds_left = self.rounds_total

    def add_player(self, player: Player):
        self.players.append([player, 0]) # second argument is the score

    def player_count(self):
        return len(self.players)

    def get_suisse_sorted_players(self):
        s = sorted(self.players, key=lambda player: player[0].rank, reverse=True)  # sort by score
        return sorted(s, key=lambda player: player[1], reverse=True)  # sort by rank
        # return sorted(self.players, key=itemgetter(1, 2), reverse=True)

    def create_round(self):
        self.rounds_left -= 1
        round_name = 'Round' + str(self.rounds_total - self.rounds_left)
        round = Round(round_name)
        self.rounds.append(round)
        return round

    def generate_matches(self):
        matches = []
        round = self.create_round()
        players = self.get_suisse_sorted_players()
        if self.rounds_total - self.rounds_left == 1:
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
                del players[0]
                del players[y]

        round.add_matches(matches)

    def played_against(self, player_one, player_two):
        opposition = []
        for round in self.rounds:
            for matches in round.matches:
                opposition.append([matches[0][0], matches[1][0]])

        return [player_one, player_two] in opposition or [player_two, player_one] in opposition


