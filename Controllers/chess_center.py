from Models.Tournament import Tournament


def tournament_creation():
    name = input('What\'s the name of the tournament?')
    place = input('Where does the tournament take place?')
    date = input('When?')
    round_number = input('Number of round?')
    return Tournament(name, place, date, round_number)


def main():
    tournament = tournament_creation()
    print('Le tournoi', tournament.name, 'débute', tournament.date, 'à', tournament.place, '\n',
           'il y aura', tournament.rounds_number, 'tours')

if __name__ == "__main__":
    main()
