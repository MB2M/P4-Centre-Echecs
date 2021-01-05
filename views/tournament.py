from models.tournament import Tournament
from models.round import Round
from models.match import Match


def launch():
    print('===============')
    print('Tournament Menu')
    print('===============')
    print('    0) <== Back')
    print('    1) Create a new tournament')
    print('    2) Open a tournament')
    print('    6) Reports')


def menu(tournament: Tournament):
    print('====================================================')
    print('Tournament : ' + tournament.name)
    print('====================================================')
    print('    0) <== Back')
    if tournament.rounds_left == 0:
        print('*** Tournament is over ***')
    elif len(tournament.players) < 2 * tournament.rounds_total:
        print('*** Add',
              str(tournament.rounds_total * 2 - tournament.player_count()),
              'players before generating rounds ***')
        print('    1) Add players')
    else:
        if not tournament.rounds or tournament.rounds[-1].is_closed():
            print('    2) Generate next round', '({} round(s) left)'.format(tournament.rounds_left))
        else:
            print('*** Running round : ' + tournament.rounds[-1].name)
            print('    3) Enter scores for current round')
            if tournament.rounds[-1].total_scores() == tournament.rounds_total:
                print('    4) Close current round')


def scoring_menu(round: Round):
    print('----------------------------------------------------')
    print('SCORING the round : ' + round.name)
    print('----------------------------------------------------')
    print('Choose the match to score :')
    print('    0) <== Back')
    for i, match in enumerate(round.matches, start=1):
        print('    ' + str(i) + ') ' + match.result_menu[0][0].first_name + ',' + match.result_menu[0][0].last_name + ' [' + str(match.result_menu[0][1]) + '] vs. ['
              + str(match.result_menu[1][1]) + ']' + match.result_menu[1][0].first_name + ',' + match.result_menu[1][0].last_name)


def result_menu(match: Match):
    print('    0) <== Back')
    print('    1) Winner : ' + match.result[0][0].first_name + ',' + match.result[0][0].first_name)
    print('    2) Winner : ' + match.result[1][0].first_name + ',' + match.result[1][0].first_name)
    print('    3) Draw')
    print('    4) Unset')


def tournaments(tournaments):
    print('    0) <== Back')
    for i, tournament in enumerate(tournaments, start=1):
        print('    ' + str(i) + ') ' + tournament.name)
