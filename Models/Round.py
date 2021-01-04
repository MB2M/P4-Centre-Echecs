from Models.Match import Match
from datetime import datetime


class Round:
    def __init__(self, name):
        self.name = name
        self.closed = False
        self.start_date = datetime.now()
        self.matchs = []

    def close(self):
        self.closed = True
        self.end_time = datetime.now()

    def add_match(self, match: Match):
        self.match.append(match)
