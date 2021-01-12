from tinydb import TinyDB


class Player:
    class Decorators(object):
        @classmethod
        def to_db(cls, func):
            def save_into_db(*args, **kwargs):
                func(*args, **kwargs)
                serialized_players = [
                    player.serialize()
                    for player in Player.PLAYERS
                ]
                db = TinyDB('db.json')
                players_table = db.table('players')
                players_table.truncate()
                players_table.insert_multiple(serialized_players)
            return save_into_db

    PLAYERS = []

    def __init__(self, last_name, first_name, birthday, gender, rank):
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.gender = gender
        self.rank = rank

    def __str__(self):
        return self.last_name + ' , ' + self.first_name

    @classmethod
    @Decorators.to_db
    def add_player(cls, player):
        cls.PLAYERS.append(player)

    @classmethod
    def get_player(cls, index):
        return cls.PLAYERS[index]

    @classmethod
    def get_all(cls):
        return cls.PLAYERS

    @classmethod
    def get_all_by_rank(cls):
        return sorted(cls.get_all(),
                      key=lambda player: int(player.rank),
                      reverse=True)

    @classmethod
    def get_all_by_alpha(cls):
        return sorted(cls.get_all(), key=lambda player: str(player))

    @Decorators.to_db
    def set_rank(self, rank):
        self.rank = rank

    def serialize(self):
        return {
            'last_name': self.last_name,
            'first_name': self.first_name,
            'birthday': self.birthday,
            'gender': self.gender,
            'rank': self.rank
        }

    @classmethod
    def deserialize(cls, serialized_player):
        last_name = serialized_player['last_name']
        first_name = serialized_player['first_name']
        birthday = serialized_player['birthday']
        gender = serialized_player['gender']
        rank = serialized_player['rank']
        return Player(last_name, first_name, birthday, gender, rank)

    @classmethod
    def save_all_to_db(cls):
        serialized_players = [player.serialize() for player in cls.PLAYERS]
        db = TinyDB('db.json')
        players_table = db.table('players')
        players_table.truncate()
        players_table.insert_multiple(serialized_players)

    @classmethod
    def load_all_from_db(cls):
        cls.PLAYERS = []
        db = TinyDB('db.json')
        players_table = db.table('players')
        serialized_players = players_table.all()
        for serialized_player in serialized_players:
            player = Player.deserialize(serialized_player)
            Player.add_player(player)

    def to_report(self):
        return {
            'last_name': self.last_name,
            'first_name': self.first_name,
            'birthday': self.birthday,
            'gender': self.gender,
            'rank': self.rank
        }
