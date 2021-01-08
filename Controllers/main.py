import re

import pandas as pd

from controllers import player as player_controller,\
    tournament as tournament_controller
from models.tournament import Tournament
from models.player import Player
from views import main as main_view


def index():
    Player.load_all_from_db()
    Tournament.load_all_from_db()
    main_view.launch()
    return menu()


def menu():
    main_view.menu()
    choice = input()
    if choice == '1':
        return player_controller.index()
    elif choice == '2':
        return tournament_controller.index()
    elif choice == '3':
        return report_index()
    elif choice == '4':
        return end()
    else:
        print('incorrect choice !')
        return menu()


def end():
    return main_view.end()


def report_index():
    main_view.report_menu()
    choice = input()
    if choice == '0':  # back last Menu
        return index()
    if choice == '1':
        players = Player.get_all_by_alpha()
        report(players)
    if choice == '2':
        players = Player.get_all_by_rank()
        report(players)
    if choice == '3':
        tournament_id = tournament_controller.select_tournament()
        if tournament_id is not None:
            tournament = Tournament.get_tournament(tournament_id)
            tournament_players = tournament.get_players_by_alpha()
            players = [
                Player.get_player(player)
                for player in tournament_players
            ]
            report(players)
    if choice == '4':
        tournament_id = tournament_controller.select_tournament()
        if tournament_id is not None:
            tournament = Tournament.get_tournament(tournament_id)
            tournament_players = tournament.get_players_by_rank()
            players = [
                Player.get_player(player)
                for player in tournament_players
            ]
            report(players)
    if choice == '5':
        tournaments = Tournament.TOURNAMENT
        if len(tournaments) > 0:
            report(tournaments)
    if choice == '6':
        tournament_id = tournament_controller.select_tournament()
        if tournament_id is not None:
            tournament = Tournament.get_tournament(tournament_id)
            rounds = tournament.rounds
            report(rounds)
    if choice == '7':
        tournament_id = tournament_controller.select_tournament()
        if tournament_id is not None:
            tournament = Tournament.get_tournament(tournament_id)
            matches = []
            for rnd in tournament.rounds:
                for match in rnd.matches:
                    matches.append(match)
                    # matches.append(match.result_to_string())
            report(matches)
    input('Press ENTER to continue')
    return report_index()


def report(list_of_element):
    data = [element.to_report() for element in list_of_element]
    df = pd.DataFrame(data)
    print(df)


def input_new_or_current(input_text, current_value, regex=None):
    value = input_regex(input_text, regex) if regex else input(input_text)
    if value == '':
        value = current_value
    return value


def input_regex(input_text, regex):
    val = input(input_text)
    if regex is not None and not re.match(regex, val):
        raise ValueError("Value entered is not correct")
    return val


def loop_conditional_input(input_text, regex, error_text, current_value=None):
    while True:
        try:
            if current_value is None:
                val = input_regex(input_text, regex)
            else:
                val = input_new_or_current(input_text, current_value, regex)
            break
        except ValueError:
            print('* {} *'.format(error_text))
    return val


def input_with_options(
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
                    return input_regex(input_text, regex)
                else:
                    return input_new_or_current(
                        input_text,
                        current_value,
                        regex
                    )
            except ValueError:
                print('* {} *'.format(error_text))
    else:
        try:
            if current_value is None:
                return input_regex(input_text, regex)
            else:
                return input_new_or_current(input_text, current_value, regex)
        except ValueError:
            print('* {} *'.format(error_text))
