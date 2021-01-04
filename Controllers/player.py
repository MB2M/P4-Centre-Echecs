from models.player import Player
from views import player as player_view


def index():
    player_view.launch()
    print('player controller')


def add_player():
    last_name = input('Last name : ')
    first_name = input('First name : ')
    birthday = input('Birthday (dd/mm/aaaaa) : ')
    gender = input('gender (m/w) : ')
    rank = input('rank : ')
    player = Player(last_name, first_name, birthday, gender, rank)
    save_db(player)

    return player


def save_db(player: Player):
    # save to db
    pass


def get_player(ind: int):
    # find player into db by index
    pass


def all_players():
    return Player.get_all()


def show_all_players():
    player_view.list_of_players(all_players())


def edit_rank(player: Player):
    player_view.rank(player)
    rank = input()
    player.rank = rank
    save_db(player)
