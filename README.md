
# World Of Games (WoG)  
#### CLI gaming platform that allows player to choose and play a command line based game.
this project was created during DevOps training course and demonstrates Python coding, working with Flask and HTML page creation and publishing.

The program will install all needed python module dependencies, Prompt user to enter player name (will be recorded for leaderboard) and display the playable games menu. 

Player will need to choose a game and difficulty level. 
Python flask module is used to display the leaderboard  on HTML web page and can be accessed from: 127.0.0.1:30000 once running. 

If WoG platform is run using the built in **bat / sh** files the web page will automatically open in the default browser. Once closed, the platform and the flask application will be purged from active memory and will no longer be accessible .


**_this project it is still a work in progress_**



## Environment and minimum requirements

The platform was made compatible with Windows, Linux, Mac operating systems CLI.

the platform was written is python3.8 code infrastructure, as such 
Python 3.8 and pip installer must be present on system.




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


