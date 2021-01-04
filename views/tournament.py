from models.tournament import Tournament


def launch():
    print('===========')
    print('Tournament')
    print('===========')
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
    print('    3) Create rounds')
