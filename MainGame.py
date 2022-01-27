'''
This is the main game platform executable. world of games is a gaming platform
that enables to run games added to its library
'''
################################################
### this part installs all the prerequisites ###
################################################
import subprocess
import sys

command = [
    sys.executable,
    '-m',
    'pip',
    'install',
    '-r',
    'requirements.txt',
]
subprocess.check_call(command)
################################################
################################################
from Data import Utils, Live
import importlib
from Data.Live import menu_list as game_list


def get_player():
    Utils.clearConsole()
    player_name = input(" Enter player Name: ")
    return player_name

def sub_menu(player, game):
    Utils.clearConsole()
    print(f'''Good game, \033[1;31m{player}\033[0m.
    1 - Play \033[1;41m{game.__name__}\033[0m again 
    2 - Main menu
    3 - Change Player
    4 - Exit\n''')
    choice = ""
    index = 1
    while not choice.isnumeric() or 0 >= int(choice) or int(choice) > 4:
        if index == 2:
            print('\033[F' + '\033[K' + '\033[F')
        choice = input("Enter selection: ")
        index = 2
    if int(choice) == 4:
        Live.exit()
    elif int(choice) == 1:
        return int(choice)
    elif int(choice) == 2:
        start = main(player)
        Play(start[0], start[1], start[2])
    elif int(choice) == 3:
        player_name = get_player()
        start = main(player_name)
        Play(start[0], start[1], start[2])



def main(player):
    Live.welcome(player)
    result = Live.Choose_game()
    game_to_play = importlib.import_module(f'Data.Games.{game_list[result[0]-1]}')
    game_difficulty = result[1]
    return game_to_play, game_difficulty, player


def Play(game, difficulty, player):
    res = game.play(difficulty)
    if res is False:
        print('''
        
                    \033[4;35mSorry, you Lose.\033[0m\n
        ''')
        Utils.counter(3)
        again = sub_menu(player, game)
        if again == 1:
            Play(game, difficulty, player)
    else:
        print('''
        
                    \033[4;32mWinner, Winner, Chicken Dinner\033[0m\n
        ''')
        Utils.counter(3)
        again = sub_menu(player, game)
        if again == 1:
            Play(game, difficulty, player)


player_name = get_player()
start = main(player_name)
Play(start[0], start[1], start[2])
