'''
This will initialize the requirements
'''
################################################
### this part installs all the prerequisites ###
################################################
from Data import Utils
import subprocess, sys

command = [
    sys.executable,
    '-m',
    'pip',
    'install',
    '-r',
    'Data/requirements.dat'
]
try:
    subprocess.check_call(command, stdout=subprocess.DEVNULL)
except Exception as er:
    Utils.error_logging(f"""{Utils.BAD_RETURN_CODE["2001"]}\nErrorHandle: {er}""")
    sys.exit("Check error log file")
################################################
################################################
