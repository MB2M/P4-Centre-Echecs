def launch():
    print('===========')
    print('Player Menu')
    print('===========')
    print('    0) <== Back')
    print('    1) Create a Player')
    print('    2) Edit player rank')


def list_of_players(players):
    for i, player in enumerate(players, start=1):
        print(i, ":", player.first_name, ',', player.last_name)


def rank(player):
    print(player.first_name, ',', player.last_name)
    print('Actual Rank :', player.rank)
    print('Enter new rank: ')
