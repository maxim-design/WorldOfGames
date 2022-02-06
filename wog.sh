python3 initialize.py
python3 Leaderboard.py &>/dev/null &
open http://127.0.0.1:30000/
python3 MainGame.py
kill -9 $PPID
