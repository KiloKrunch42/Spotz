import RPi.GPIO as GPIO
from time import sleep


# basic setup
def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.IN)


def measure():
    signal = GPIO.input(14)

    return signal


if __name__ == '__main__':
    setup()
    print("For debug purposes the script will print out the sensor readings every 5 seconds. Stop with Ctrl + c")
    while True:
        output = measure()
        print(output)
        sleep(5)
