# WorldOfGames (WoG) - CLI gaming platform
this project was created during DevOps training course and demonstrates Python coding, working with Flask and HTML page publishing  - Work in progress

the platform is made compatible with Windows, Linux, Mac operating systems CLI. 

will open a cli window, install all needed dependencies, and prompt for player name.
After name was excepted will display the WoG platform menu that will be compiled form the list of all the games available in the “..\Data\Games” folder.
New games can be added by adding the python game module files into the “..\Data\Games“ Of the WoG platform. 
New game modules must contain:
“about” function that returns 2 vales: Game name. Game description.
“play” function that returns 2 values: result (True/False)  -  for game won or lost
          Correct answer       -  the initially created correct answer generated  by the game.  
Player will be prompted to select game to play and the difficulty level at which point the game will run. 
After each game player score will be accumulated as long as the player is still playing and update is sent live to the leaderboard html page created with flask. (top 10 players scores are displayed)
Errors are stored for review in error-log file in platform directory. 

--- this is still a work in progress -- 
