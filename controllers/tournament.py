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
        return manage(tournament)
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


def manage(tournament: Tournament):
    tournament_view.menu(tournament)
    choice = input()

    if choice == '0':  # back last Menu
        return index()

    if tournament.player_count() < 2 * tournament.rounds_total:
        player = None
        if choice == '1':  # Create player
            player = player_controller.add_player()
            tournament.add_player(player)
    elif not tournament.rounds or tournament.rounds[-1].is_closed():
        if choice == '2':
            tournament.generate_matches()
    else:
        if choice == '3':
            return match_index(tournament, tournament.rounds[-1])
        if choice == '4' and tournament.rounds[-1].total_scores() == tournament.rounds_total:
            tournament.rounds[-1].close()

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
    return match_index(tournament, round)


def tournament_index():
    tournaments = Tournament.TOURNAMENT
    tournament_view.tournaments(tournaments)
    choice = input()
    if choice == '0':
        return main_controller.index()
    return Tournament.get_tournament(int(choice) - 1)
