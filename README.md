![image](https://user-images.githubusercontent.com/97593405/157765848-53b2e1a3-c233-4a60-9513-c60f4443fa73.png)

# World Of Games (WoG)  
#### CLI gaming platform that allows player to choose and play a command line based game.
this project was created during DevOps training course and demonstrates **Python** coding, working with **Flask** and **HTML** page creation and publishing, as well as using **Docker** (& Docker-compose) to package the app into a container and running it in a **Jenkins Pipeline** with some **Selenium** tests on the games scoreboard.  

The program will install all needed python module dependencies, Prompt user to enter player name (will be recorded for leaderboard) and display the playable games menu. 

Player will need to choose a game and difficulty level. 
Python flask module is used to display the leaderboard  on HTML web page and can be accessed from: 127.0.0.1:30000 once running. 

## Execution

WoG platform can be run localy using the built in **bat / sh** files. The web page will automatically open in the default browser showing the Leader board. Once closed, the platform and the flask application will be purged from active memory and will no longer be accessible .




## Environment and minimum requirements

The platform was made compatible with **Windows**, **Linux**, **Mac** operating systems CLI.

the platform was written is python3.8 code infrastructure, as such 
Python 3.8 and pip installer must be present on system.

Jenkins and Docker are needed to run the testing pipeline.

[![python](https://user-images.githubusercontent.com/97593405/157931793-17ac9e96-93e6-40ec-9e12-6b612d157d35.png)][1][![docker](https://user-images.githubusercontent.com/97593405/157931835-9583e015-793d-4777-9dc3-8e8a23661bd0.png)][2][![jenkins](https://user-images.githubusercontent.com/97593405/157931843-2c274077-857d-43e4-9e75-14ac02d3f7fc.png)][3]

[1]: https://www.python.org/downloads/release/python-380/
[2]: https://www.docker.com/products/docker-desktop
[3]: https://www.jenkins.io/download/


## Features

- self compiling games menu (will include all .py modules present in the `../WorldOfGames/Data/Games/` folder.)

- Continuously updating leader board with html output. (top 10 players) 

- execution scripts for automatic platform start (wog.bat / wog.sh)



    ### Adding new games to the platform

    The platform was designed to allow easy game addition by including a new game file into the 
    `../WorldOfGames/Data/Games/` folder. The game must be written in python 3.8 compatible script,
    must be named `somename.py`and has to contain the following functions:
    **about()**  -  returning 2 variables: game_name, game_description
    example:
    ```python3.8
    def about():
   	    game_name = "NewGame"
    	game_description = "This game does this and that"
        return game_name, game_description
    ```
    **play(difficulty)** - gets the difficulty  as an **_integer_** variable and returning 2 variables: game result, correct answer
    ```python3.8
    def play(difficulty):
        correct_answer = computer generated something based on difficulty.
        user_input = some user input
        “some code that does something based on game rules”
        Result = true or false based on user_input vs correct_answer.
        return result, correct_answer
    ```	


