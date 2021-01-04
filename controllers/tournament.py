from controllers import main as main_controller
from models.tournament import Tournament
from models.player import Player
from views import tournament as tournament_view
from views import player as player_view


def index():
    tournament_view.launch()
    choice = input()
    if choice == '0':
        return main_controller.index()
    if choice == '1':
        tournament = new()
        if tournament:
            return menu(tournament)
    elif choice == '2':
        return print("TODO: choix 2")
    else:
        return index()


def new():
    name = input('Tournament name : ')
    place = input('Tournament place : ')
    date = input('Tournament date : ')
    round_number = input('Number of rounds : ')

    return Tournament(name, place, date, round_number)


def menu(tournament: Tournament):
    tournament_view.menu(tournament)
    choice = input()
    if choice == '0':
        return index()
    if choice == '1':
        last_name = input('Last name : ')
        first_name = input('First name : ')
        birthday = input('Birthday (dd/mm/aaaaa) : ')
        gender = input('gender (m/w) : ')
        rank = input('rank : ')
    elif choice == '2':
        player_view.list_of_players()
        player_index = input()
        # Récupère les attributs du player depuis la  DB
    elif choice == '3':
        return create_round(tournament)
    else:
        return menu(tournament)
    player = Player(last_name, first_name, birthday, gender, rank)
    tournament.add_player(player)
    return menu(tournament)


def create_round():
    pass