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

    date_regex = '^(0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/[0-9]{4}$'

    match = None
    while not match:
        date_start = input('Tournament start date : ')
        match = re.match(date_regex, date_start)

    match = None
    while not match:
        date_end = input('End date ? (Empty if it\'s a 1-day tournament) ')
        match = re.match(date_regex, date_end)
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
    tournament = Tournament(name, place, date, time_control,
                            description, round_number)

    Tournament.add_tournament(tournament)
    return tournament


def manage(tournament: Tournament):
    tournament_view.menu(tournament)
    choice = input()
    if choice == '9':  #
        leaderboard(tournament)

    if choice == '0':  # back last Menu
        return index()
    if choice == '1':
        edit(tournament)
    if tournament.player_count < 2 * tournament.rounds_total:
        if choice == '2':  # load a player
            player_id = player_controller.select_player()
            if player_id is not None:
                tournament.add_player(player_id)
    elif not tournament.rounds or tournament.rounds[-1].is_closed():
        if choice == '3':  # generate matches
            tournament.generate_matches()
    else:
        if choice == '4':  # score match of current round
            return match_index(tournament, tournament.rounds[-1])
        if (
                choice == '5' and
                tournament.rounds[-1].total_scores() == tournament.rounds_total
        ):  # close current round
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
    if (
            not re.match('^[0-9]+$', choice)
            or int(choice) not in range(len(Tournament.TOURNAMENT) + 1)
    ):
        return select_tournament()
    return int(choice) - 1


def leaderboard(tournament):
    for player in tournament.get_suisse_sorted_players():
        print('[{}]'.format(player[1]), Player.get_player(player[0]).name)


def edit(tournament):
    tournament.name = input_new_or_current(
        'Name [{}] : '.format(tournament.name),
        tournament.name
    )
    tournament.place = input_new_or_current(
        'Tournament place [{}] : '.format(tournament.place),
        tournament.place
    )

    date_regex_or_current = re.compile(r'^[\w|\W]*$|^(0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/[0-9]{4}$')

    date_start = input_new_or_current(
        'Tournament start date [{}] : '.format(tournament.date),
        tournament.date,
        date_regex_or_current
    )

    if 'to' in date_start:
        match = None
        while not match:
            date_end = input('End date ? (Empty if it\'s a 1-day tournament) ')
            match = re.match(date_regex_or_current, date_end)
        tournament.date = date_start
        if date_end != "":
            tournament.date += 'to ' + date_end

        tournament.rounds_total = int(input_new_or_current(
            'Number of rounds [{}] : '.format(tournament.rounds_total),
            tournament.rounds_total,
            re.compile(r'^[1-3]+$|^[\w|\W]*$')
        ))

    tournament.description = input_new_or_current(
        'Current description :\n {} \n'.format(tournament.description),
        tournament.description
    )

    tournament.time_control = input_new_or_current(
        'Time control [{}] : \n'
        '    1) Bullet\n'
        '    2) Blitz\n'
        '    3) Rapid\n'.format(tournament.time_control),
        tournament.time_control,
        re.compile(r'^[1-3]+$|^[\w|\W]*$')
    )


def input_new_or_current(input_text, current_value, regex=re.compile(r'^[\w|\W]*$')):

    value = input_regex(input_text, regex)
    if input_text == '':
        value = current_value
    return value


def input_regex(input_text, regex):
    match = None
    while not match:
        value = input(input_text)
        print(value)
        match = re.match(regex, value)

    return value
