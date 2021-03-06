'''
This is the main platform executable. world of games is a gaming platform
that enables to run python writen games added to its library
'''
from Data import Utils, Live, Players_Data
import importlib, initialize
from Data.Live import menu_list as game_list
from pygame import mixer

current_total = 0
mixer.init()
mixer.music.load("Data/Sound/gamesound.wav") # Paste The audio file location 
mixer.music.play(-1) 

def get_player():
    global current_total
    current_total = 0
    Utils.clearConsole()
    Utils.banner()
    player_n = " "
    index_a = 1
    while Utils.string_check(player_n):
        if index_a == 2:
            print('\033[F' + '\033[K' + '\033[F')
        player_n = input(" Enter player Name: ")
        index_a = 2
    return player_n


def sub_menu(player, game):
    Utils.clearConsole()
    Utils.banner()
    GameName = game.about()
    print(f"Good game, \033[1;31m{player}\033[0m. Your current score: \033[93m{current_total}\033[0m\n")
    choice_list2 = [f'Play {GameName[0]} again (same difficult)', 'Back to games menu', 'New player']
    choice_sub = Utils.show_menu(choice_list2)
    if int(choice_sub) == 3:
        player_name = get_player()
        start = main(player_name)
        Play(start[0], start[1], start[2])
    elif int(choice_sub) == 1:
        return int(choice_sub)
    elif int(choice_sub) == 2:
        start = main(player)
        Play(start[0], start[1], start[2])


def main(player):
    Live.welcome(player)
    result = Live.Choose_game()
    game_to_play = importlib.import_module(f'Data.Games.{game_list[result[0]-1]}')
    game_difficulty = result[1]
    return game_to_play, game_difficulty, player


def Play(game, difficulty, player):
    global current_total
    try:
        res = game.play(difficulty)
    except Exception as Perr:
        Utils.error_logging(f"""{Utils.BAD_RETURN_CODE["4003"]}{game}\nErrorHandle: {Perr}""")
        print("\033[1;31mError Playing the Game - check logs.\033[0m.")
        Live.exit()
    if res[0] is False:
        print(f'''

                    \033[4;35mSorry, you Lose.\033[0m\n
                        the right answer was: {res[1]}
        ''')
        Utils.counter(5)
        again = sub_menu(player, game)
        if again == 1:
            Play(game, difficulty, player)
    else:
        current_total = current_total + Players_Data.gameScore_calc(difficulty)
        Players_Data.apply_current_score_to_player(player, current_total)
        print(f'''
        
                    \033[4;32mWinner, Winner, Chicken Dinner\033[0m\n
        ''')
        Utils.counter(3)
        again = sub_menu(player, game)
        if again == 1:
            Play(game, difficulty, player)

player_name = get_player()
start = main(player_name)
Play(start[0], start[1], start[2])
