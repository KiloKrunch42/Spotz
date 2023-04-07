import pathlib
from datetime import datetime


def log(text):
    directory = pathlib.Path(__file__).parent.absolute()
    log_file = open(str(directory) + "/log.txt", 'a')
    dt = datetime.now()
    log_file.write(str(dt) + ": " + str(text) + "\n")
    log_file.close()
