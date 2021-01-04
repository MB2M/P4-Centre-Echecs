class Tournament:
    def __init__(self, name, place, date, rounds_number=4):
        self.name = name
        self.place = place
        self.date = date
        self.rounds_number = rounds_number
        self.rounds = []
        self.players = []
        self.time_control = "bullet"
        self._description = ""

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, text):
        self.description = text

