import configparser
import pathlib
import smtplib
from email.message import EmailMessage


def read_config(file):
    config = configparser.ConfigParser()
    config.read(file)

    return config


def create_message(config, subject, content):
    msg = EmailMessage()
    msg.set_content(content)

    msg['Subject'] = subject
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
    directory = pathlib.Path(__file__).parent.absolute()
    user_config = read_config(str(directory) + '/config.ini')
    message = create_message(user_config)
    send_message(message, user_config)
