import sensor
import mailer
from time import sleep
import os

if __name__ == '__main__':
    sensor.setup()
    user_config = mailer.read_config(os.getcwd() + '/config.ini')
    while True:
        if sensor.measure() == 1:
            mailer.send_message(mailer.create_message(user_config), user_config)
            # We only want to send mails again after the sensor has dried again...
            while sensor.measure() == 1:
                sleep(300)
            # TODO: Logging
        # TODO: The sleep value could also be provided per a section in the config.ini
        sleep(300)
