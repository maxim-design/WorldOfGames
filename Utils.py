'''
This is the utility file for the World of Games platform.
'''
import os, time


def clearConsole():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def counter(number):
    for i in range(number, 0, -1):
        print(f"Just a sec, {i}", end="\r", flush=True)
        time.sleep(1)


if __name__ == "__main__":
    print("This file needs to be run from MainGame.py thank and have a nice day")
    input("Press Enter to continue...")
