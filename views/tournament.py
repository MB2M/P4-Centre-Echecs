def launch():
    print(
        '===============',
        'Tournament Menu',
        '===============',
        '    0) <== Back',
        '    1) Create a new tournament',
        '    2) Load a tournament',
        sep='\n'
    )


def menu(tournament):
    print(
        '====================================================',
        'Tournament : ' + tournament.name,
        '====================================================',
        '    0) <== Back',
        '    1) Edit tournament settings',
        sep='\n'
    )
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
    print(
        '----------------------------------------------------',
        'SCORING the round : ' + round.name,
        '----------------------------------------------------',
        'Choose the match to score :',
        '    0) <== Back',
        sep='\n'
    )
    for i, match in enumerate(round.matches, start=1):
        print('    ' + str(i) + ') ' + match.result_to_string())


def result_menu(match):
    print(
        'Choose the result of the match :',
        '    0) <== Back',
        '    1) Winner : ' + match.get_player_name(match.player_one),
        '    2) Winner : ' + match.get_player_name(match.player_two),
        '    3) Draw',
        '    4) Unset',
        sep='\n'
    )


def tournaments(tournaments):
    print('    0) <== Back')
    for i, tournament in enumerate(tournaments, start=1):
        print('    ' + str(i) + ') ' + tournament.name)
