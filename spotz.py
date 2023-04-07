import sensor
import mailer
import pathlib
from datetime import datetime
from time import sleep


def log(text):
    directory = pathlib.Path(__file__).parent.absolute()
    log_file = open(str(directory) + "/log.txt", 'a')
    dt = datetime.now()
    log_file.write(str(dt) + ": " + str(text) + "\n")
    log_file.close()


if __name__ == '__main__':
    log("Spotz started")
    sensor.setup()
    current_dir = pathlib.Path(__file__).parent.absolute()
    user_config = mailer.read_config(str(current_dir) + '/config.ini')
    subject = f'Wasserstandswarnung'
    message = 'Beep Boop\nAchtung! Der Wasserstand hat den Sensor erreicht!\nStatus Füße: Nass' \
              '\nBitte Hausratsversicherung prüfen!\nBoop Beep'
    while True:
        if sensor.measure() == 1:
            log("Water sensor triggered")
            mailer.send_message(mailer.create_message(user_config, subject, message), user_config)
            # We only want to send mails again after the sensor has dried again...
            while sensor.measure() == 1:
                sleep(300)
        # TODO: The sleep value could also be provided per a section in the config.ini
        sleep(300)
