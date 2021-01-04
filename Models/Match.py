from Models.Player import Player

class Match:
    def __init__(self, player_one: Player, player_one_score, player_two: Player, player_two_score):
        self.result = ([player_one, player_one_score], [player_two, player_two_score])
