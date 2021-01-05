class Player:
    PLAYERS = []

    def __init__(self, last_name, first_name, birthday, gender, rank):
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.gender = gender
        self.rank = rank

    @classmethod
    def add_player(cls, player):
        cls.PLAYERS.append(player)

    @classmethod
    def get_all(cls):
        return cls.PLAYERS

    @classmethod
    def get_all_by_rank(cls):
        return sorted(cls.get_all(), key=lambda player: player['rank'], reverse=True)

    @classmethod
    def get_all_by_alpha(cls):
        s = sorted(cls.get_all(), key=lambda player: player['first_name'])
        return sorted(s, key=lambda player: player['last_name'])


