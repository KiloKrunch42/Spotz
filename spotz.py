import sensor
import mailer
import pathlib
from datetime import datetime
from time import sleep


def log(text):
    dir = pathlib.Path(__file__).parent.absolute()
    logFile = open(str(dir) + "/log.txt", 'a')
    dt = datetime.now()
    logFile.write(str(dt) + ": " + str(text) + "\n")
    logFile.close()


if __name__ == '__main__':
    log("Spotz started")
    sensor.setup()
    dir = pathlib.Path(__file__).parent.absolute()
    user_config = mailer.read_config(str(dir) + '/config.ini')
    while True:
        if sensor.measure() == 1:
            log("Water sensor triggered")
            mailer.send_message(mailer.create_message(user_config), user_config)
            # We only want to send mails again after the sensor has dried again...
            while sensor.measure() == 1:
                sleep(300)
        # TODO: The sleep value could also be provided per a section in the config.ini
        sleep(300)
