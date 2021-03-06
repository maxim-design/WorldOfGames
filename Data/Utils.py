'''
This is the utility file for the World of Games platform.
'''
from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint

import os, time, datetime, re

def show_menu(choice_list):
    style = style_from_dict({
        Token.QuestionMark: '#000000',
        Token.Selected: 'bg:#00aaaa #000000',
        Token.Pointer: '#000000',
        Token.Instruction: '',  # default
        Token.Answer: '#000000',
        Token.Question: '',
    })
    question_1 = [
        {
            'type': 'list',
            'name': 'choice',
            'message': " ",
            'choices': choice_list
        }
    ]
    answer_1 = prompt(question_1, style=style)
    choice = int(choice_list.index(answer_1['choice']))+1
    return choice

def clearConsole():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def counter(number):
    for i in range(number, 0, -1):
        print(f"Just a sec, {i}", end="\r", flush=True)
        time.sleep(1)

def error_logging(error):
  path = "Data/error-log"
  now = str(datetime.datetime.now())
  os.makedirs(path, exist_ok=True)
  with open('Data/error-log/error.log', 'a') as f:
    f.write(now + ": " + error + "\n")
    f.close()

BAD_RETURN_CODE = {"2001": "Cannot install requirements!",
                   "3001": "cannot open playerdata.dat (scores file). check file exists/corrupted",
                   "4001": "Game module doesn't contain an appropriate about() function. cannot add to menu module: ",
                   "4002": "Failed importing game module. check that game module is in the correct python format.",
                   "4003": "Game module Play function is corrupted or doesnt exist. check game module: "}

def banner():
    print('''
    ██╗    ██╗ \033[96m██████╗ ██████╗ ██╗ \033[94m    ██████╗      ██████╗ ███████╗   \033[93m  ██████╗  █████╗ ███╗   ███╗███\033[96m████╗███████╗\033[0m
    ██║    █\033[96m█║██╔═══██╗██╔══██╗\033[94m██║     ██╔══██╗    ██╔═══██╗██╔═══\033[93m═╝    ██╔════╝ ██╔══██╗████╗ ████║\033[96m██╔════╝██╔════╝\033[0m
    ██║ █\033[96m╗ ██║██║   ██║██████\033[94m╔╝██║     ██║  ██║    ██║   ██║██\033[93m███╗      ██║  ███╗███████║██╔████╔\033[96m██║█████╗  ███████\033[0m╗
    ██║\033[96m███╗██║██║   ██║██╔═\033[94m═██╗██║     ██║  ██║    ██║   \033[93m██║██╔══╝      ██║   ██║██╔══██║██║╚█\033[96m█╔╝██║██╔══╝  ╚════█\033[0m█║
    ╚\033[96m███╔███╔╝╚██████╔╝██\033[94m║  ██║███████╗██████╔╝    ╚███\033[93m███╔╝██║         ╚██████╔╝██║  ██║██\033[96m║ ╚═╝ ██║███████╗████\033[0m███║
    \033[96m ╚══╝╚══╝  ╚═════╝\033[94m ╚═╝  ╚═╝╚══════╝╚═════╝      ╚\033[93m═════╝ ╚═╝          ╚═════╝ ╚═╝  ╚═╝\033[96m╚═╝     ╚═╝╚══════╝╚══\033[0m════╝                                                                                                                                       
       \033[0m\n''')

def string_check(user_input):
    if not re.match("^[A-Z,0-9,a-z,-]*$", user_input):
        return True
    elif len(user_input) > 20:
        return True


if __name__ == "__main__":
    print("This file needs to be run from MainGame.py thank and have a nice day")
    input("Press Enter to continue...")
