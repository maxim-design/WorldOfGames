'''
WoG Menu compiler and library. will compile the list of games based on library /Games content.
adding a game has never been easier. Simply place the new game module into /Games directory.
important note:
          each game MUST contain,
          "about" function - returns 2 values (name, description)
          "play" function - returns 2 values, boolean value True / False if the game won or lost and the correct answer.
'''
from Data import Utils
import sys, os

############################################################################
######################### Games library list  ##############################
Live_path = os.path.dirname(os.path.realpath(__file__))
menu_list = [".".join(f.split(".")[:-1]) for f in os.listdir(f'{Live_path}/Games') if os.path.isfile(os.path.join(f'{Live_path}/Games', f))]
menu_list.remove("__ init __")
############################################################################
############################################################################

for game in menu_list:
  try:
    exec("from Data.Games import {module}".format(module=game))
  except Exception as e:
    err = (f'{e} could not be loaded. {Utils.BAD_RETURN_CODE["4001"]}')
    Utils.error_logging(err)

menu = {}
for i in menu_list:
  try:
    exec("a={module}.about()".format(module=i))
    menu.update({a[0]:a[1]})
  except Exception as er:
    err2 = (f'could not load "{er}" description, {Utils.BAD_RETURN_CODE["4002"]}')
    Utils.error_logging(err2)
menu.update({'Exit':'Quit playing World of Games (WoG)'})


def welcome(name):
  Utils.clearConsole()
  Utils.banner()
  print(f"""Hello \033[1;31m{name}\033[0m and welcome to the World of Games (WoG).
Here you can find many cool games to play, your score will increase or decrease as you play the games.\n""")


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
    #dst = f'{os.curdir}/Games'
    files = [f for f in os.listdir(f'{os.curdir}/Games') if os.path.isfile(os.path.join(f'{os.curdir}/Games', f))]
    files.remove("__ init __.py")
    print(list(files))
    print("This file needs to be run from MainGame.py thank and have a nice day")
    input("Press Enter to continue...")
