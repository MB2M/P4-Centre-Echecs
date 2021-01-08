from models.player import Player


class Match:
    def __init__(self, player_one_id, player_two_id, score_one=0, score_two=0):
        self.player_one = player_one_id
        self.player_two = player_two_id
        self.score_one = score_one
        self.score_two = score_two

    def set_result(self, score_one, score_two):
        self.score_one = score_one
        self.score_two = score_two

    @property
    def result(self):
        return [self.player_one, self.score_one], \
               [self.player_two, self.score_two]

    def total_score(self):
        return self.score_one + self.score_two

    def result_to_string(self):
        return (Player.get_player(self.result[0][0]).name
                + ' [{}] vs. [{}] '.format(self.score_one, self.score_two)
                + Player.get_player(self.result[1][0]).name
                )

    def serialize(self):
        return {'result': self.result}

    @classmethod
    def deserialize(cls, serialized_match):
        player_one = serialized_match['result'][0][0]
        player_two = serialized_match['result'][1][0]
        score_one = serialized_match['result'][0][1]
        score_two = serialized_match['result'][1][1]
        return Match(player_one, player_two, score_one, score_two)

    def to_report(self):
        return {
            'Player One': Player.get_player(self.player_one).name,
            'Score': "{} - {}".format(self.score_one, self.score_two),
            'Player Two': Player.get_player(self.player_two).name,
        }
