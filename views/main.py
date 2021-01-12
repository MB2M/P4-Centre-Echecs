class ViewMain:

    @staticmethod
    def launch():
        print(
            '========================================',
            'Welcome to your Chess Tournament Manager',
            '========================================',
            sep='\n'
            )

    @staticmethod
    def menu():
        print(
            'What do you want to do?',
            '    1) Player Manager',
            '    2) Tournament Manager',
            '    3) Report',
            '    4) Exit Program',
            sep='\n'
        )

    @staticmethod
    def end():
        print(
            '=============================================',
            'Thank you for using Chess Tournament Manager ',
            '=============================================',
            sep='\n'
            )

    @staticmethod
    def report_menu():
        print('    0) <== Back',
              '    1) List of players by alpha',
              '    2) List of players by rank',
              '    3) List of tournament\'s players by alpha',
              '    4) List of tournament\'s players by rank',
              '    5) List of all tournaments',
              '    6) List of tournament\' rounds',
              '    7) List of tournament\' matches',
              sep='\n'
              )
