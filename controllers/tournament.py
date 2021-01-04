from controllers import main as main_controller
from controllers import player as player_controller
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from views import tournament as tournament_view
from views import player as player_view


def index():
    tournament_view.launch()
    choice = input()
    if choice == '0':  # back last Menu
        return main_controller.index()
    if choice == '1':  # Create Tournament
        tournament = new()
        if tournament:
            return menu(tournament)
    elif choice == '2':  # Retrieve Tournament
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

    if choice == '0':  # back last Menu
        return index()
    if choice == '1':  # Create player
        player = player_controller.add_player()
    elif choice == '2':  # Retrieve player
        player_view.list_of_players()
        player_index = input()
        # Récupère les attributs du player depuis la  DB et l'instancie
        # player
    elif choice == '3':
        tournament.generate_matches()
        return menu(tournament)
    elif choice == '4':
        return scoring_menu(tournament)
    else:
        return menu(tournament)

    tournament.add_player(player)
    return menu(tournament)


def scoring_menu(tournament: Tournament):
    tournament_view.scoring_menu(tournament)
    choice = input()
    if choice == '0':  # back last Menu
        return menu(tournament)
    for i, round in enumerate(tournament.rounds, start=1):
        if choice == str(i):
            return scoring(tournament, round)

    return scoring_menu(tournament)


def scoring(tournament: Tournament, round: Round):
    tournament_view.scoring(round)
    choice = input()
    if choice == '0':  # back last Menu
        return scoring_menu(tournament)
    for i, match in enumerate(round.matches, start=1):
        if choice == str(i):
            return result(tournament, round, match)


def result(tournament: Tournament, round: Round, match: Match):
    tournament_view.result(match)
    choice = input()
    if choice == '0':  # back last Menu
        return scoring(tournament, round)
    if choice == '1':
        match.set_result(1, 0)
    elif choice == '2':
        match.set_result(0, 1)
    elif choice == '3':
        match.set_result(0.5, 0.5)
    elif choice == '4':
        match.set_result(0, 0)
    else:
        return result(tournament, round, match)

    tournament.update_players_score()
    return scoring(tournament, round)
