def launch():
    print('===========')
    print('Player Menu')
    print('===========')
    print('    0) <== Back')
    print('    1) Create a player')
    print('    2) Edit player rank')


def rank(player):
    print('Edit rank :')
    print('-----------')
    print(player.first_name, ',', player.last_name)
    print('Actual Rank :', player.rank)
    print('Enter new rank: ')


def players(players):
    print('Select a player :')
    print('    0) <== Back')
    for i, player in enumerate(players, start=1):
        print('    ' + str(i) + ') ' + player.name)
