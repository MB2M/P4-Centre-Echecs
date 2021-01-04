from models.player import Player


class Tournament:
    def __init__(self, name, place, date, rounds_number=4):
        self.name = name
        self.place = place
        self.date = date
        self.rounds_number = rounds_number
        self.rounds = []
        self.players = []
        self.time_control = "bullet"
        self.description = ""

    def add_player(self, player: Player):
        self.players.append(player)

    def player_count(self):
        return len(self.players)

