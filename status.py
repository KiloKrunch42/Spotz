import mailer
import pathlib
import time
from logger import log


def status():
    uptime = time.clock_gettime(time.CLOCK_BOOTTIME)
    days = int(uptime // 86400)
    seconds_left = uptime % 86400
    hours = int(seconds_left // 3600)
    minutes = int(round((seconds_left % 3600)/60, 0))
    status_message = 'Hier spricht der Sumpenpumpf! Ich lebe noch. Es ist dunkel hier unten. ' \
                     'Ich arbeite nun schon unterbrechungsfrei seit ' + str(days) + ' Tagen, ' \
                     + str(hours) + ' Stunden und ' + str(minutes) + \
                     ' Minuten.\nWäre ich doch bloß in eine Gewerkschaft eingetreten... :('

    return status_message


if __name__ == '__main__':
    log("Status function called")
    current_dir = pathlib.Path(__file__).parent.absolute()
    user_config = mailer.read_config(str(current_dir) + '/config.ini')

    subject = f'Statusbericht Sumpenpumpf'
    message = status()
    mailer.send_message(mailer.create_message(user_config, subject, message), user_config)
