import re

import pandas as pd

from .player import PlayerController
from .tournament import TournamentController
from models.player import Player
from models.tournament import Tournament
from views.main import ViewMain


class MainController:

    def index(self):
        Player.load_all_from_db()
        Tournament.load_all_from_db()
        ViewMain.launch()
        return self.menu()

    def menu(self):
        ViewMain.menu()
        choice = input()
        if choice == '1':
            return PlayerController().index()
        elif choice == '2':
            return TournamentController().index()
        elif choice == '3':
            return self.report_index()
        elif choice == '4':
            return self.end()
        else:
            print('incorrect choice !')
            return self.menu()

    def end(self):
        return ViewMain.end()

    def report_index(self):
        ViewMain.report_menu()
        choice = input()
        if choice == '0':  # back last Menu
            return self.index()
        if choice == '1':
            players = Player.get_all_by_alpha()
            self.report(players)
        if choice == '2':
            players = Player.get_all_by_rank()
            self.report(players)
        if choice == '3':
            tournament_id = TournamentController().select_tournament()
            if tournament_id is not None:
                tournament = Tournament.get_tournament(tournament_id)
                tournament_players = tournament.get_players_by_alpha()
                players = [
                    Player.get_player(player)
                    for player in tournament_players
                ]
                self.report(players)
        if choice == '4':
            tournament_id = TournamentController().select_tournament()
            if tournament_id is not None:
                tournament = Tournament.get_tournament(tournament_id)
                tournament_players = tournament.get_players_by_rank()
                players = [
                    Player.get_player(player)
                    for player in tournament_players
                ]
                self.report(players)
        if choice == '5':
            tournaments = Tournament.TOURNAMENT
            if len(tournaments) > 0:
                self.report(tournaments)
        if choice == '6':
            tournament_id = TournamentController().select_tournament()
            if tournament_id is not None:
                tournament = Tournament.get_tournament(tournament_id)
                rounds = tournament.rounds
                self.report(rounds)
        if choice == '7':
            tournament_id = TournamentController().select_tournament()
            if tournament_id is not None:
                tournament = Tournament.get_tournament(tournament_id)
                matches = []
                for rnd in tournament.rounds:
                    for match in rnd.matches:
                        matches.append(match)
                        # matches.append(match.result_to_string())
                self.report(matches)
        input('Press ENTER to continue')
        return self.report_index()

    def report(self, list_of_element):
        data = [element.to_report() for element in list_of_element]
        df = pd.DataFrame(data)
        print(df)

    def input_new_or_current(self, input_text, current_value, regex=None):
        if regex:
            value = self.input_regex(input_text, regex)
        else:
            value = input(input_text)
        if value == '':
            value = current_value
        return value

    def input_regex(self, input_text, regex):
        val = input(input_text)
        if regex is not None and not re.match(regex, val):
            raise ValueError("Value entered is not correct")
        return val

    def loop_conditional_input(self, input_text, regex,
                               error_text, current_value=None):
        while True:
            try:
                if current_value is None:
                    val = self.input_regex(input_text, regex)
                else:
                    val = self.input_new_or_current(input_text,
                                                    current_value,
                                                    regex)
                break
            except ValueError:
                print('* {} *'.format(error_text))
        return val

    def input_with_options(
            self,
            input_text,
            regex=None,
            error_text="",
            current_value=None,
            loop=False
    ):
        if loop:
            while True:
                try:
                    if current_value is None:
                        return self.input_regex(input_text, regex)
                    else:
                        return self.input_new_or_current(
                            input_text,
                            current_value,
                            regex
                        )
                except ValueError:
                    print('* {} *'.format(error_text))
        else:
            try:
                if current_value is None:
                    return self.input_regex(input_text, regex)
                else:
                    return self.input_new_or_current(input_text,
                                                     current_value,
                                                     regex)
            except ValueError:
                print('* {} *'.format(error_text))
