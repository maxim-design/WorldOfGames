import json, os.path
from os import path


def gameScore_calc(difficulty):
    game_score = (difficulty * 3) + 5
    return game_score


def apply_current_score_to_player(player_name, newscore):

    def previous_score_smaller(name, currentscore):
        if data[f"{name}"] < currentscore:
            return True
        else:
            return False

    basedata = {"WoG":0}
    newdata = {f"{player_name}":newscore}
    player_name = (list(newdata.keys()))[0]
    newscore = (list(newdata.values()))[0]

    try:
        with open('Data/playerdata.dat') as json_file:
            data = json.load(json_file)
    except:
        with open('Data/playerdata.dat', 'w', encoding='utf-8') as f:
            json.dump(basedata, f, ensure_ascii=False, indent=4)
        with open('Data/playerdata.dat') as json_file:
            data = json.load(json_file)

    ammountOFkeys = len(data.keys())
    if ammountOFkeys < 10:
        if player_name in data:
            if previous_score_smaller(player_name, newscore):
                data.update(newdata)
        else:
            data.update(newdata)
    elif ammountOFkeys == 10:
        if player_name in data:
            if previous_score_smaller(player_name, newscore):
                data.update(newdata)
        else:
            lastscore = (list(data.values()))[9]
            if newscore > lastscore:
                del data[(list(data.keys()))[9]]
                data.update(newdata)


    tempDict = {}

    sortedList=sorted(data.values())
    reversedList=reversed(sortedList)

    for sortedKey in reversedList:
        for key, value in data.items():
            if value==sortedKey:
                tempDict[key]=value
        with open('Data/playerdata.dat', 'w', encoding='utf-8') as f: json.dump(tempDict, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    print("This file needs to be run from MainGame.py thank and have a nice day")
    input("Press Enter to continue...")
