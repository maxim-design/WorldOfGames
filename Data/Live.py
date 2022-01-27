'''
WoG Menu compiler and library. will compile the list of games based on library list.
adding a game has never been easier.
'''
from Data import Utils
import sys
import os, datetime

############################################################################
##################### Games library list  ##############################
'''
This section contains the game module names in the game list that populates the 
main menu. To add another game just add its module name here.
note: a game must contain about(), play(difficulty) functions.
about - returns to the platform name, description valuables. (to populate the menu)
play  - will execute the game with difficulty and return True/False for win or lose.
'''
#import MemoryGame, GuessGame, CurrencyRouletteGame
menu_list = ['MemoryGame', 'GuessGame', 'CurrencyRouletteGame']

############################################################################
############################################################################


def error_logging(error):
  path = "error-log"
  now = str(datetime.datetime.now())
  os.makedirs(path, exist_ok=True)
  with open('error-log/error.log', 'a') as f:
    f.write(now + ": " + error + "\n")
    f.close()


for game in menu_list:
  try:
    exec("from Data.Games import {module}".format(module=game))
  except Exception as e:
    err = (f"{e} could not be loaded. check specific game file.")
    error_logging(err)

menu = {}
for i in menu_list:
  try:
    exec("a={module}.about()".format(module=i))
    menu.update({a[0]:a[1]})
  except Exception as er:
    err2 = (f'could not load "{er}" description, make sure the "about" function is present and correctly returns data')
    error_logging(err2)
menu.update({'Exit':'Quit playing World of Games (WoG)'})


def welcome(name):
  Utils.clearConsole()
  print(f"""Hello \033[1;31m{name}\033[0m and welcome to the World of Games (WoG).
Here you can find many cool games to play.\n""")


def exit():
  input('''\n\033[1;94mThank you for playing World of Games (WoG). Come back soon.
Consider making a donation so we can make more fun games a reality at:
imaginary_Donations.wishfullthinking/never-gonna-happen :P\033[0m.
Press Enter to close''')
  sys.exit()


def Choose_game():
  line=1
  print("\033[4;94mPlease Choose a game to play:\033[0m\n")
  for key, value in menu.items():
    print(f"{line}.", key, ' - ', value)
    line+=1
  print("\n")
  choice = ""
  index = 1
  while not choice.isnumeric() or 0 >= int(choice) or int(choice) > len(menu.keys()):
    if index == 2:
      print('\033[F' + '\033[K' + '\033[F')
    choice = input("Enter selection: ")
    index = 2
  if int(choice) == len(menu.keys()):
    exit()
  else:
    difficulty = ""
    index_b = 1
    while not difficulty.isnumeric() or 0 >= int(difficulty) or int(difficulty) > 5:
      if index_b == 2:
        print('\033[F' + '\033[K' + '\033[F')
      difficulty = input("Input difficulty level between 1-5: ")
      index_b = 2
  return int(choice), int(difficulty)


if __name__ == "__main__":
    print("This file needs to be run from MainGame.py thank and have a nice day")
    input("Press Enter to continue...")
