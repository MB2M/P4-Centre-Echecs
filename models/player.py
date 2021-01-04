class Player:
    def __init__(self, last_name, first_name, birthday, gender, rank):
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.gender = gender
        self.rank = rank

    @classmethod
    def get_all(cls):
        pass
