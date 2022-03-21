import sqlite3, json, os.path
from os import path



def create_sql_db(dictdata):
    playerscores = dictdata
    keys = list(playerscores.keys())
    del keys[0]
    first = (list(playerscores.keys())[0])
    firstvalue = playerscores[first]
    values = list(playerscores.values())
    del values[0]

    conn = sqlite3.connect('./Data/playerdata.dat')

    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS playerscores")
    c.execute(f'CREATE TABLE playerscores ({first} text) ')
    c.execute(f'INSERT INTO playerscores ({first}) values ({firstvalue})')

    for i in keys:
        c.execute(f'ALTER TABLE playerscores ADD COLUMN "{(i)}" text')
        conn.commit()

    for i in keys:  
        c.execute(f'UPDATE playerscores SET "{i}" = ("{values[keys.index(i)]}")')

    conn.commit()
    conn.close()

def load_sql_into_dict():
    SQLDB = "./Data/playerdata.dat"
    conn = sqlite3.connect( SQLDB )
    conn.row_factory = sqlite3.Row
    db = conn.cursor()
    db.execute('SELECT * from playerscores')
    rows = db.fetchall()
    for t in rows:
        newdata = dict(t)
    for key in newdata:
        newdata[key] = int(newdata[key])
    return newdata

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
        data =load_sql_into_dict()
    except:
        create_sql_db(basedata)
        data = load_sql_into_dict()
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
    create_sql_db(tempDict)

if __name__ == "__main__":
    print("This file needs to be run from MainGame.py thank and have a nice day")
    input("Press Enter to continue...")
