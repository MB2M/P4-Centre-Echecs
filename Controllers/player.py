import re

from controllers import main as main_controller
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
    last_name = input('Last name : ')
    first_name = input('First name : ')

    match = None
    while not match:
        birthday = input('Birthday (dd/mm/yyyy) : ')
        match = re.match('^(0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/[0-9]{4}$', birthday)

    gender = input('gender (m/w) : ')
    while gender not in ['m', 'w']:
        gender = input('gender (m/w) : ')

    match = None
    while not match:
        rank = input('rank : ')
        match = re.match('^[0-9]+$', rank)
    player = Player(last_name, first_name, birthday, gender, rank)

    Player.add_player(player)


def edit_rank(player: Player):
    player_view.rank(player)
    match = None
    while not match:
        rank = input()
        match = re.match('^[0-9]+$', rank)
    player.set_rank(rank)


def player_index():
    players = Player.PLAYERS
    player_view.players(players)


def select_player():
    player_index()
    choice = input()
    if choice == '0':
        return None
    if not re.match('^[0-9]+$', choice) or int(choice) not in range(len(Player.PLAYERS) + 1):
        return select_player()
    return int(choice)-1
