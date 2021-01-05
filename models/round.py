from datetime import datetime

from models.match import Match


class Round:
    def __init__(self, name):
        self.name = name
        self.start_date = datetime.now()
        self.matches = []
        self.end_time = False

    def close(self):
        self.end_time = datetime.now()

    def add_match(self, match: Match):
        self.matches.append(match)

    def add_matches(self, matches: list):
        for match in matches:
            self.matches.append(match)

    def is_closed(self):
        return self.end_time

    def total_scores(self):
        return sum(match.total_score() for match in self.matches)