from models.player import Player


class Match:
    def __init__(self, player_one: Player, player_two: Player):
        self.result = ([player_one, None], [player_two, None])

    def set_result(self, score_a, score_b):
        self.result[0][1] = score_a
        self.result[1][1] = score_b
