from controllers import player
from controllers import tournament
from views import main as menu_view


def index():
    menu_view.launch()
    return menu()


def menu():
    menu_view.menu()
    choice = input()
    if choice == '1':
        return player.index()
    elif choice == '2':
        return tournament.index()
    elif choice == '3':
        return end()
    else:
        print('choix incorrect !')
        return menu()


def end():
    return menu_view.end()
