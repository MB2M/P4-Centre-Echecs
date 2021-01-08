import re

from controllers2 import player as player_controller, \
    main as main_controller
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
    name = main_controller.input_with_options('Tournament name : ')
    place = main_controller.input_with_options('Tournament place : ')

    date_regex = re.compile(r'^(0[1-9]|[1-2][0-9]|3[0-1])/'
                            r'(0[1-9]|1[0-2])/[0-9]{4}$')
    date_start = main_controller.input_with_options(
        'Tournament start date : ',
        date_regex,
        'Date format should be: dd/mm/yyyy',
        loop=True
    )
    date_end_regex = re.compile(r'^(0[1-9]|[1-2][0-9]|3[0-1])/'
                                r'(0[1-9]|1[0-2])/[0-9]{4}$|^$')
    date_end = main_controller.input_with_options(
        'End date ? (Empty if it\'s a 1-day tournament) : ',
        date_end_regex,
        'Date format should be: dd/mm/yyyy',
        loop=True
    )
    date = date_start
    if date_end != "":
        date += ' to ' + date_end

    round_number = main_controller.input_with_options(
        'Number of rounds : ',
        re.compile('^[0-9]+$'),
        'Please enter a positive number',
        loop=True
    )

    description = main_controller.input_with_options('description : ')

    time_control_list = ['Bullet', 'Blitz', 'Rapid']
    text = 'Time control [{}] : \n'
    for i in range(len(time_control_list)):
        text += '    ' + str(i) + ') ' + time_control_list[i] + '\n'
    time_control = main_controller.input_with_options(
        text,
        re.compile(r'^[1-3]+$|^[\w|\W]*$'),
        'Please enter 1, 2 or 3',
        loop=True
    )
    if time_control in ['1', '2', '3']:
        time_control = time_control_list[int(time_control) - 1]

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
    tournament.name = main_controller.input_with_options(
        'Name [{}] : '.format(tournament.name),
        current_value=tournament.name
    )
    tournament.place = main_controller.input_with_options(
        'Tournament place [{}] : '.format(tournament.place),
        current_value=tournament.place
    )

    date_regex_or_current = re.compile(r'^[\w|\W]*$|'
                                       r'^(0[1-9]|[1-2][0-9]|3[0-1])'
                                       r'/(0[1-9]|1[0-2])/[0-9]{4}$')

    date_start = main_controller.input_with_options(
        'Tournament start date [{}] : '.format(tournament.date),
        date_regex_or_current,
        'Please enter a date format (dd/mm/yyyy)',
        tournament.date,
        True,
    )
    tournament.date = date_start

    date_end = main_controller.input_with_options(
        'End date ? (Empty if it\'s a 1-day tournament) ',
        date_regex_or_current,
        'Please enter a date format (dd/mm/yyyy)',
        loop=True
    )

    if date_end != '':
        tournament.date += ' to ' + date_end

    tournament.rounds_total = int(
        main_controller.input_with_options(
            'Number of rounds [{}] : '.format(tournament.rounds_total),
            re.compile(r'^[1-3]+$|^[\w|\W]*$'),
            'Please enter a positive number',
            tournament.rounds_total,
            True
        )
    )

    tournament.description = main_controller.input_with_options(
        'Current description :\n {} \n'.format(tournament.description),
        current_value=tournament.description
    )

    time_control_list = ['Bullet', 'Blitz', 'Rapid']
    text = 'Time control [{}] : \n'
    for i in range(len(time_control_list)):
        text += '    ' + str(i) + ') ' + time_control_list[i] + '\n'
    time_control = main_controller.input_with_options(
        text.format(tournament.time_control),
        re.compile(r'^[1-3]+$|^[\w|\W]*$'),
        'Please enter 1, 2 or 3',
        tournament.time_control,
        True
    )
    if time_control in ['1', '2', '3']:
        tournament.time_control = time_control_list[int(time_control) - 1]
