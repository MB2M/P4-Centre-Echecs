import re

from controllers import main as main_controller
from controllers import player as player_controller
from models.match import Match
from models.player import Player
from models.round import Round
from models.tournament import Tournament
from views import tournament as tournament_view


def index():
    tournament_view.launch()
    choice = input()
    if choice == '0':  # back last Menu
        return main_controller.index()
    if choice == '1':  # Create Tournament
        tournament = new()
        return manage(tournament)
    elif choice == '2':  # Retrieve Tournament
        tournament_id = select_tournament()
        if tournament_id is not None:
            tournament = Tournament.get_tournament(tournament_id)
            return manage(tournament)
    return index()


def new():
    name = input('Tournament name : ')
    place = input('Tournament place : ')
    match = None
    while not match:
        date_start = input('Tournament date : ')
        match = re.match('^(0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/[0-9]{4}$', date_start)

    match = None
    while not match:
        date_end = input('End date ? (Leave empty if it\'s a 1-day tournament) ')
        match = re.match('^(0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/[0-9]{4}$|$', date_end)
    date = date_start
    if date_end != "":
        date += 'to ' + date_end

    match = None
    while not match:
        round_number = input('Number of rounds : ')
        match = re.match('^[0-9]+$', round_number)

    description = input('description : ')

    match = None
    while not match:
        time_control = input('Time control : \n'
                             '    1) Bullet\n'
                             '    2) Blitz\n'
                             '    3) Rapid\n'
                             )
        match = re.match('^[1-3]+$', time_control)
    tournament = Tournament(name, place, date, time_control, description, round_number)

    Tournament.add_tournament(tournament)
    return tournament


def manage(tournament: Tournament):
    tournament_view.menu(tournament)
    choice = input()
    if choice == '9':  #
        leaderboard(tournament)

    if choice == '0':  # back last Menu
        return index()

    if tournament.player_count < 2 * tournament.rounds_total:
        player = None
        if choice == '1':  # load a player
            player_id = player_controller.select_player()
            if player_id is not None:
                tournament.add_player(player_id)
    elif not tournament.rounds or tournament.rounds[-1].is_closed():
        if choice == '2':  # generate matches
            tournament.generate_matches()
    else:
        if choice == '3':  # score match of current round
            return match_index(tournament, tournament.rounds[-1])
        if choice == '4' and tournament.rounds[-1].total_scores() == tournament.rounds_total:  # close current round
            tournament.close_last_round()

    return manage(tournament)


def match_index(tournament: Tournament, round: Round):
    tournament_view.scoring_menu(round)
    choice = input()
    if choice == '0':  # back last Menu
        return manage(tournament)
    for i, match in enumerate(round.matches, start=1):
        if choice == str(i):
            return score(tournament, round, match)


def score(tournament: Tournament, round: Round, match: Match):
    tournament_view.result_menu(match)
    choice = input()
    if choice == '0':  # back last Menu
        return match_index(tournament, round)
    if choice == '1':
        match.set_result(1, 0)
    elif choice == '2':
        match.set_result(0, 1)
    elif choice == '3':
        match.set_result(0.5, 0.5)
    elif choice == '4':
        match.set_result(0, 0)
    else:
        return score(tournament, round, match)

    tournament.update_players_score()
    # Tournament.save_all_to_db()
    return match_index(tournament, round)


def tournament_index():
    tournaments = Tournament.TOURNAMENT
    tournament_view.tournaments(tournaments)


def select_tournament():
    tournament_index()
    choice = input()
    if choice == '0':
        return None
    if not re.match('^[0-9]+$', choice) or int(choice) not in range(len(Tournament.TOURNAMENT) + 1):
        return select_tournament()
    return int(choice) - 1


def leaderboard(tournament):
    for player in tournament.get_suisse_sorted_players():
        print('[{}]'.format(player[1]), Player.get_player(player[0]).name)
