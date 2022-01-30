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


BAD_RETURN_CODE = {"3001": "cannot create/write to scores file. check access/permissions.",
                   "4001": "Game Module doesn't contain an appropriate about() function. cannot add to menu module: ",
                   "4002": "Game Module Play function is corrupted or doesnt exist. check game module: "}


if __name__ == "__main__":
    print("This file needs to be run from MainGame.py thank and have a nice day")
    input("Press Enter to continue...")
