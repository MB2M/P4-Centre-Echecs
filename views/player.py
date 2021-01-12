class ViewPlayer:

    @staticmethod
    def launch():
        print(
            '===========',
            'Player Menu',
            '===========',
            '    0) <== Back',
            '    1) Create a player',
            '    2) Edit player rank',
            sep='\n'
        )

    @staticmethod
    def rank(player):
        print('Edit rank :',
              '-----------',
              player,
              'Actual Rank :', player.rank,
              'Enter new rank: ',
              sep='\n'
              )

    @staticmethod
    def players(players):
        print(
            'Select a player :',
            '    0) <== Back',
            sep='\n'
        )
        for i, player in enumerate(players, start=1):
            print('    ' + str(i) + ') ', player)
