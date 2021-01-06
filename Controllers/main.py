import pandas as pd

from controllers import main as main_controller
from controllers import player as player_controller
from controllers import tournament as tournament_controller
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
        print('choix incorrect !')
        return menu()


def end():
    return main_view.end()


def report_index():
    main_view.report_menu()
    choice = input()
    if choice == '0':  # back last Menu
        return main_controller.index()
    if choice == '1':
        players = Player.get_all_by_alpha()
        report(players, 'players')
    if choice == '2':
        players = Player.get_all_by_rank()
        report(players, 'players')
    if choice == '3':
        tournament_id = tournament_controller.select_tournament()
        if tournament_id is not None:
            tournament = Tournament.get_tournament(tournament_id)
            tournament_players = tournament.get_players_by_alpha()
            players = [Player.get_player(player) for player in tournament_players]
            report(players, 'players')
    if choice == '4':
        tournament_id = tournament_controller.select_tournament()
        if tournament_id is not None:
            tournament = Tournament.get_tournament(tournament_id)
            tournament_players = tournament.get_players_by_rank()
            players = [Player.get_player(player) for player in tournament_players]
            report(players, 'players')
    if choice == '5':
        tournaments = Tournament.TOURNAMENT
        if len(tournaments) > 0:
            report(tournaments, 'tournaments')
    if choice == '6':
        tournament_id = tournament_controller.select_tournament()
        if tournament_id is not None:
            tournament = Tournament.get_tournament(tournament_id)
            rounds = tournament.rounds
            report(rounds, 'rounds')
    if choice == '7':
        tournament_id = tournament_controller.select_tournament()
        if tournament_id is not None:
            tournament = Tournament.get_tournament(tournament_id)
            matches = []
            for round in tournament.rounds:
                for match in round.matches:
                    matches.append(match)
                    # matches.append(match.result_to_string())
            report(matches, 'matches')
    input('Press ENTER to continue')
    return report_index()


def report(list_of_objects, type):
    if type == 'players':
        columns = ['last_name', 'first_name', 'birthday', 'gender', 'rank']

    elif type == 'tournaments':
        columns = ['name', 'date']

    data = [object.to_report() for object in list_of_objects]

    df = pd.DataFrame(data)
    # df = pd.DataFrame([vars(object) for object in list_of_objects])
    print(df)

