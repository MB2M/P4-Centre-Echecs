import re

from . import main
from models.player import Player
from views.player import ViewPlayer


class PlayerController:
    def index(self):
        ViewPlayer.launch()
        choice = input()
        if choice == '0':
            return main.MainController().index()
        elif choice == '1':
            self.add_player()
        elif choice == '2':
            player_id = self.select_player()
            if player_id is not None:
                player = Player.get_player(player_id)
                self.edit_rank(player)
        return self.index()

    def add_player(self):
        c = main.MainController()
        last_name = c.input_with_options('Last name : ')
        first_name = c.input_with_options('First name : ')

        date_regex = re.compile(r'^(0[1-9]|[1-2][0-9]|3[0-1])'
                                r'/(0[1-9]|1[0-2])/[0-9]{4}$')
        birthday = c.input_with_options(
            'Birthday (dd/mm/yyyy) : ',
            date_regex,
            'Please enter a valid date format (dd/mm/yyyy)',
            loop=True
        )
        gender = c.input_with_options(
            'gender (m/w) : ',
            re.compile(r'^[m|w]$'),
            'Please enter m or w',
            loop=True
        )

        rank = c.input_with_options(
            'Current rank : ',
            re.compile('^[0-9]+$'),
            'Please enter en positive number',
            loop=True
        )

        player = Player(last_name, first_name, birthday, gender, rank)

        Player.add_player(player)

    def edit_rank(self, player: Player):
        c = main.MainController()
        ViewPlayer.rank(player)
        rank = c.input_with_options(
            '',
            re.compile('^[0-9]+$'),
            'Please enter en positive number',
            loop=True
        )
        player.set_rank(rank)

    def player_index(self):
        players = Player.PLAYERS
        ViewPlayer.players(players)

    def select_player(self):
        self.player_index()
        choice = input()
        if choice == '0':
            return None
        if (
                not re.match('^[0-9]+$', choice)
                or int(choice) not in range(len(Player.PLAYERS) + 1)
        ):
            return self.select_player()
        return int(choice)-1
