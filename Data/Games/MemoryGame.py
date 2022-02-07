'''
Memory game for WoG platform.
about function returns game name, description
play(difficulty) function will run the game.
'''

import random
from Data import Utils
import time


def about():
    game_name = "Memory Game"
    game_description = "a sequence of numbers will appear for a time and you have to guess it back"
    return game_name, game_description

def generate_sequence(difficulty):
    Utils.clearConsole()
    computer_list = []
    for a in range(0, difficulty):
        computer_list.append(random.randint(1, 101))
    print("\n                                  \033[4;94mMemory Game\033[0m\n ")
    print(f"""Hi,
I thought of a list of number/s based on the difficulty selected.
so that difficulty level 1 will have 1 number and so on. 
the numbers will appear on screen for a peek and then be gone. 
Try to remember them as well as you can.  
good luck.\n""")
    input("Press Enter to start!")
    for b in computer_list:
        print(f" {b}", end=" ")
    print(" ", end="")
    time.sleep(1.25)
    print("", end="\r")
    time.sleep(1.25)
    tuple(computer_list)
    return computer_list


def get_list_from_user():
    userguess = input("Enter your guess: ").split(' ')
    test = 2
    ints = []
    while test == 2:
        try:
            ints = [int(item) for item in userguess]
            test = 1
        except:
            print('\033[F' + '\033[K' + '\033[F')
            userguess = input("Enter your guess (must be numbers): ").split(' ')
    tuple(ints)
    return ints


def is_list_equal(computer_selection, user_guess):
    computer_selection.sort()
    user_guess.sort()
    if user_guess == computer_selection:
        return True
    else:
        return False


def play(difficulty):
    a = generate_sequence(difficulty)
    b = get_list_from_user()
    result = is_list_equal(a, b)
    attempt = 1
    while result is False and attempt <= 2:
        if attempt == 2:
            clue = list(set(a).intersection(set(b)))
            left = len(a) - len(clue)
            print(f"\nthis is hard, here is a clue: these are the numbers you guessed right \033[4;94m{clue}\033[0m, you are missing {left} numbers")
        print("\033[1;31mWrong Answer\033[0m, try again\n")
        b = get_list_from_user()
        result = is_list_equal(a, b)
        attempt = attempt + 1
    return result, a


if __name__ == "__main__":
    print("This file needs to be run from MainGame.py thank and have a nice day")
    input("Press Enter to continue...")
