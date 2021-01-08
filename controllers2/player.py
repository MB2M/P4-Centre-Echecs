import re

from controllers2 import main as main_controller
from models.player import Player
from views import player as player_view


def index():
    player_view.launch()
    choice = input()
    if choice == '0':
        return main_controller.index()
    elif choice == '1':
        add_player()
    elif choice == '2':
        player_id = select_player()
        if player_id is not None:
            player = Player.get_player(player_id)
            edit_rank(player)
    return index()


def add_player():
    last_name = main_controller.input_with_options('Last name : ')
    first_name = main_controller.input_with_options('First name : ')

    date_regex = re.compile(r'^(0[1-9]|[1-2][0-9]|3[0-1])'
                            r'/(0[1-9]|1[0-2])/[0-9]{4}$')
    birthday = main_controller.input_with_options(
        'Birthday (dd/mm/yyyy) : ',
        date_regex,
        'Please enter a valid date format (dd/mm/yyyy)',
        loop=True
    )
    gender = main_controller.input_with_options(
        'gender (m/w) : ',
        re.compile(r'^[m|w]$'),
        'Please enter m or w',
        loop=True
    )

    rank = main_controller.input_with_options(
        'Current rank : ',
        re.compile('^[0-9]+$'),
        'Please enter en positive number',
        loop=True
    )

    player = Player(last_name, first_name, birthday, gender, rank)

    Player.add_player(player)


def edit_rank(player: Player):
    player_view.rank(player)
    rank = main_controller.input_with_options(
        '',
        re.compile('^[0-9]+$'),
        'Please enter en positive number',
        loop=True
    )
    player.set_rank(rank)


def player_index():
    players = Player.PLAYERS
    player_view.players(players)


def select_player():
    player_index()
    choice = input()
    if choice == '0':
        return None
    if (
            not re.match('^[0-9]+$', choice)
            or int(choice) not in range(len(Player.PLAYERS) + 1)
    ):
        return select_player()
    return int(choice)-1
