from models.tournament import Tournament
from models.round import Round


def launch():
    print('===============')
    print('Tournament Menu')
    print('===============')
    print('    0) <== Back')
    print('    1) Create a new tournament')
    print('    2) Open a tournament')


def menu(tournament: Tournament):
    print('----------------------------------------------------')
    print('Tournament : ' + tournament.name)
    print('----------------------------------------------------')
    print('There is', tournament.player_count(), 'player(s) registered')
    print('    0) <== Back')
    print('    1) Create players')
    print('    2) Add players from database')
    print('    3) Generate next round', '({} round(s) left)'.format(tournament.rounds_left))


def scoring_menu(tournament: Tournament):
    print('----------------------------------------------------')
    print('SCORING the tournament : ' + tournament.name)
    print('----------------------------------------------------')
    print('    0) <== Back')
    for i, round in enumerate(tournament.rounds, start=1):
        print('    ' + str(i) + ') Score round : ' + round.name)


def scoring(round: Round):
    print('----------------------------------------------------')
    print('SCORING the round : ' + round.name)
    print('----------------------------------------------------')
    print('Choose the match to score :')
    print('    0) <== Back')
    for i, match in enumerate(round.matches, start=1):
        print('    ' + str(i) + ') ' + match.result[0][0] + ' [' + match.result[0][1] + '] vs. ['
              + match.result[1][1] + ']' + match.result[1][0])
