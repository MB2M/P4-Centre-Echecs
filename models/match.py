from models.player import Player


class Match:
    def __init__(self, player_one_id, player_two_id):
        self.player_one = player_one_id
        self.player_two = player_two_id
        self.score_one = 0
        self.score_two = 0

    def set_result(self, score_one, score_two):
        self.score_one = score_one
        self.score_two = score_two

    @property
    def result(self):
        return [self.player_one, self.score_one], [self.player_two, self.score_two]

    def total_score(self):
        return self.score_one + self.score_two

    def result_to_string(self):
        return (Player.get_player(self.result[0][0]).name
                + ' [{}] vs. [{}] '.format(self.score_one, self.score_two)
                + Player.get_player(self.result[1][0]).name
                )

    # modif branch
    def serialize(self):
        return {
            'player_one': self.player_one,
            'player_two': self.player_two,
            'score_one': self.score_one,
            'score_two': self.score_two,
        }

    @classmethod
    def deserialize(cls, serialized_match):
        player_one = serialized_match['player_one']
        player_two = serialized_match['player_two']
        score_one = serialized_match['score_one']
        score_two = serialized_match['score_two']

        match = Match(player_one, player_two)
        match.set_result(score_one, score_two)
        return match

    def to_report(self):
        return {
            'match_list': self.result_to_string()
        }
