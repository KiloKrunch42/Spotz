import configparser
import os
import smtplib
from email.message import EmailMessage


def read_config(file):
    config = configparser.ConfigParser()
    config.read(file)

    return config


def create_message(config):
    msg = EmailMessage()
    msg.set_content('Achtung! Der Wasserstand hat den Sensor erreicht!')

    msg['Subject'] = f'Wasserstandswarnung'
    msg['From'] = config['Mailer']['sender']
    msg['To'] = config['Mailer']['receiver']

    return msg


def send_message(msg, config):
    # TODO: Set timeout
    # TODO: Try catch block ?!
    connection = smtplib.SMTP_SSL(host=config['Mailer']['server'], port=int(config['Mailer']['port']))
    connection.set_debuglevel(2)
    connection.login(config['Mailer']['sender'], config['Mailer']['password'])
    connection.sendmail(config['Mailer']['sender'], config['Mailer']['receiver'], msg.as_string())
    connection.quit()


if __name__ == '__main__':
    print('Mailer called directly... sending test message')
    user_config = read_config(os.getcwd() + '/config.ini')
    message = create_message(user_config)
    send_message(message, user_config)
