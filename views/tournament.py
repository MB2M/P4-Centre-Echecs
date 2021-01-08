from models.player import Player


def launch():
    print('===============')
    print('Tournament Menu')
    print('===============')
    print('    0) <== Back')
    print('    1) Create a new tournament')
    print('    2) Load a tournament')


def menu(tournament):
    print('====================================================')
    print('Tournament : ' + tournament.name)
    print('====================================================')
    print('    0) <== Back')
    print('    1) Edit tournament settings')
    if tournament.finished():
        print('*** TOURNAMENT IS OVER ***')
    elif len(tournament.players) < 2 * tournament.rounds_total:
        print('*** Add',
              str(tournament.rounds_total * 2 - tournament.player_count),
              'players before generating rounds ***')
        print('    2) Add players')
    else:
        if not tournament.rounds or tournament.rounds[-1].is_closed():
            print('    3) Generate next round')
        else:
            print('*** Running round : ' + tournament.rounds[-1].name)
            print('    4) Enter scores for current round')
            if tournament.rounds[-1].total_scores() == tournament.rounds_total:
                print('    5) Close current round')


def scoring_menu(round):
    print('----------------------------------------------------')
    print('SCORING the round : ' + round.name)
    print('----------------------------------------------------')
    print('Choose the match to score :')
    print('    0) <== Back')
    for i, match in enumerate(round.matches, start=1):
        print('    ' + str(i) + ') ' + match.result_to_string())


def result_menu(match):
    print('Choose the result of the match :')
    print('    0) <== Back')
    print('    1) Winner : ' + Player.get_player(match.result[0][0]).name)
    print('    2) Winner : ' + Player.get_player(match.result[1][0]).name)
    print('    3) Draw')
    print('    4) Unset')


def tournaments(tournaments):
    print('    0) <== Back')
    for i, tournament in enumerate(tournaments, start=1):
        print('    ' + str(i) + ') ' + tournament.name)
