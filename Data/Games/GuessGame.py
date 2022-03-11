'''
Guess Game for WoG platform.
about function returns game name, description
play(difficulty) function will run the game.
'''
import random
from Data import Utils


def about():
    game_name = "Guess Game"
    game_description = "Guess a number and see if you chose like the computer"
    return game_name, game_description



def generate_number(difficulty):
    Utils.clearConsole()
    Utils.banner()
    last = difficulty + 1
    value = random.randint(1, last)
    last_in_range = difficulty + 1
    print("\n                                  \033[4;94mGuess Game\033[0m\n ")
    print(f"""Hi,
I thought of a number between \033[4;92m1 - {last_in_range}\033[0m.
now its you job to guess what it is :)  
good luck.\n""")
    return int(value)


def get_guess_from_user():
    userguess = ""
    index = 1
    while not userguess.isnumeric():
        if index == 2:
            print('\033[F' + '\033[K' + '\033[F')
        userguess = input("Enter your guess (must be integers): ")
        index = 2
    return int(userguess)


def compare_results(computer_selection, user_guess):
    if user_guess == computer_selection:
        return True
    else:
        return False


def play(difficulty):
    a = generate_number(difficulty)
    b = get_guess_from_user()
    result = compare_results(a, b)
    attempt = 1
    while result is False and attempt <= 2:
        if attempt == 2:
            clue = abs(a - b)
            print(f"\nthis is hard, here is a clue: the distance from your last guess to my number is \033[4;94m{clue}\033[0m")
        print("\033[1;31mWrong Answer\033[0m, try again\n")
        b = get_guess_from_user()
        result = compare_results(a, b)
        attempt = attempt + 1
    return result, a


if __name__ == "__main__":
    print("This file needs to be run from MainGame.py thank and have a nice day")
    input("Press Enter to continue...")
