from models.player import Player


class Match:
    def __init__(self, player_one_id, player_two_id):
        self.result = ([player_one_id, 0], [player_two_id, 0])

    def set_result(self, score_a, score_b):
        self.result[0][1] = score_a
        self.result[1][1] = score_b

    def total_score(self):
        return self.result[0][1] + self.result[1][1]

    def result_to_string(self):
        return (Player.get_player(self.result[0][0]).name
                + ' [{}]'.format(str(self.result[0][1]))
                + ' vs. [{}] '.format(str(self.result[1][1]))
                + Player.get_player(self.result[1][0]).name
                )

    def serialize(self):
        return {'result': self.result}

    @classmethod
    def deserialize(cls, serialized_match):
        player_one_id = serialized_match['result'][0][0]
        player_two_id = serialized_match['result'][1][0]
        score_a = serialized_match['result'][0][1]
        score_b = serialized_match['result'][1][1]
        match = Match(player_one_id, player_two_id)
        match.set_result(score_a, score_b)
        return match

    def to_report(self):
        return {
            'match_list': self.result_to_string()
        }
