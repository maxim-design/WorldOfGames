echo off
python initialize.py
start "Flask" /min cmd /k "python Leaderboard.py"
start http://127.0.0.1:30000/
python MainGame.py
for /f "tokens=2 delims=," %%a in ('tasklist /fi "imagename eq cmd.exe" /v /fo:csv /nh ^| findstr /r /c:".*Flask[^,]*$" ') do taskkill /pid %%a
