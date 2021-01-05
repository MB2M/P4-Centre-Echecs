import pandas as pd

from controllers import player as player_controller
from controllers import tournament as tournament_controller
from models.tournament import Tournament
from views import main as main_view


def index():
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
        print('choix incorrect !')
        return menu()


def end():
    return main_view.end()


def report_index():
    main_view.report_menu()
    choice = input()
    if choice == '1':
        players =[]
    if choice == '2':
        players = []
    if choice == '3':
        tournament = tournament_controller.tournament_index()
        players = tournament.get_players_by_alpha()
        report(players, 'players')
    if choice == '4':
        tournament = tournament_controller.tournament_index()
        players = tournament.get_players_by_rank()
        report(player, 'players')
    if choice == '5':
        tournaments = Tournament.TOURNAMENT
        report(tournaments, 'tournaments')
    if choice == '6':
        tournament = tournament_controller.tournament_index()
        rounds = tournament.rounds
        report(rounds, 'rounds')
    if choice == '7':
        tournament = tournament_controller.tournament_index()
        matches = []
        for round in tournament.rounds:
            for match in round.matches:
                matches.append(match)
        report(matches, 'matches')
    input('Press ENTER to continue')
    return report_index()


def report(list_of_objects, type):
    if type == 'players':
        columns = ['last_name', 'first_name', 'birthday', 'gender', 'rank']

    elif type == 'tournaments':
        columns = ['name', 'date']

    df = pd.DataFrame([vars(object) for object in list_of_objects])
    print(df)

