import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class motor():
    def __init__(self, Ena, In1, In2):
        self.Ena = Ena
        self.In1 = In1
        self.In2 = In2
        GPIO.setup(self.Ena, GPIO.OUT)
        GPIO.setup(self.In1, GPIO.OUT)
        GPIO.setup(self.In2, GPIO.OUT)
        self.pwm = GPIO.PWM(self.Ena, 100)
        self.pwm.start(0)

    def moveF(self, x):
        self.pwm.ChangeDutyCycle(x)
        GPIO.output(self.In1, GPIO.HIGH)
        GPIO.output(self.In2, GPIO.LOW)

    def moveB(self, x):
        self.pwm.ChangeDutyCycle(x)
        GPIO.output(self.In1, GPIO.LOW)
        GPIO.output(self.In2, GPIO.HIGH)

    def stop(self):
        self.pwm.ChangeDutyCycle(0)


# #Define Gpio pins
# motor1 = motor(2,3,4)
# motor1.moveF(100)
# sleep(2)
# motor1.stop()
# sleep(1)
# motor1.moveB(100)
# sleep(1)
# motor1.stop()
# sleep(1)

# Define Gpio pins
motor1 = motor(2, 3, 4)
motor2 = motor(17, 27, 22)


def Forward():
    motor1.moveF(100)
    motor2.moveF(100)


def Backward():
    motor1.moveB(100)
    motor2.moveB(100)


def Stop():
    motor1.stop()
    motor2.stop()


def Left():
    motor1.moveF(100)
    motor2.moveB(100)


def Right():
    motor1.moveB(100)
    motor2.moveF(100)


while True:
    Forward()
    sleep(2)
    Backward()
    sleep(2)
    Stop()
    sleep(2)

    Left()
    sleep(2)
    Forward()
    sleep(2)

    Right()
    sleep(2)
    Forward()
    sleep(2)

    Stop()
    sleep(2)