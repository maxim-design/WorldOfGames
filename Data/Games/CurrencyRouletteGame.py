'''
Currency Roulette for WoG platform.
about function returns game name, description
play(difficulty) function will run the game.
'''
from Data import Utils
import random
import requests


def about():
    game_name = "Currency Roulette"
    game_description = "try and guess the value of a random USD amount in ILS"
    return game_name, game_description


def generate_number(difficulty):
    Utils.clearConsole()
    value = random.randint(10, 100)
    print("\n                                  \033[4;94mCurrency Roulette Game\033[0m\n ")
    print(f"""Hi,
This is an amount in USD: \033[4;92m{value}\033[0m.
now its you job to guess how much that would be in ILS (Israeli Shekel) without using any tools or websites :)  
however, based on the difficulty you selected, you'r allowed a margin of error of {5-difficulty}
good luck.\n""")
    return float(value)


def get_rate_interval(difficulty, value):
    from_ = "USD"
    to_ = "ILS"
    response = requests.get(f'https://freecurrencyapi.net/api/v2/latest?base={from_}')
    exchange_rate = response.json()['data'][to_]
    secret_ILS_value = value * exchange_rate
    interval = [float(secret_ILS_value-(5-difficulty)), float(secret_ILS_value+(5-difficulty))]
    return interval, secret_ILS_value


def is_float_digit(n) -> bool:
    try:
        float(n)
        return True
    except ValueError:
        return False


def get_guess_from_user():
    userguess = ""
    index = 1
    while not is_float_digit(userguess):
        if index == 2:
            print('\033[F' + '\033[K' + '\033[F')
        userguess = input("Enter your guess (must be real number): ")
        index = 2
    return float(userguess)


def play(difficulty):
    a = get_rate_interval(difficulty, generate_number(difficulty))
    b = get_guess_from_user()
    result = a[0][0] < b < a[0][1]
    attempt = 1
    while result is False and (attempt <= 2):
        if attempt == 2:
            clue = abs(int(a[1] - b))
            print(f"\nthis seems hard, here is a clue: your away from the answer by about \033[4;94m{clue}\033[0m")
        print("\033[1;31mWrong Answer\033[0m, try again\n")
        b = get_guess_from_user()
        result = a[0][0] < b < a[0][1]
        attempt = attempt + 1
    return result


if __name__ == "__main__":
    print("This file needs to be run from MainGame.py thank and have a nice day")
    input("Press Enter to continue...")
