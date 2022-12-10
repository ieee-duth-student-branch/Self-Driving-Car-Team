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

    def moveF(self, speed):
        self.pwm.ChangeDutyCycle(speed)
        GPIO.output(self.In1, GPIO.HIGH)
        GPIO.output(self.In2, GPIO.LOW)

    def moveB(self, speed):
        self.pwm.ChangeDutyCycle(speed)
        GPIO.output(self.In1, GPIO.LOW)
        GPIO.output(self.In2, GPIO.HIGH)

    def stop(self):
        self.pwm.ChangeDutyCycle(0)


# Define Gpio pins
motor1 = motor(2, 3, 4)
motor2 = motor(17, 27, 22)


def Forward(speed=100, t=0):
    motor1.moveF(speed)
    motor2.moveF(speed)
    sleep(t)


def Backward(speed=100, t=0):
    motor1.moveB(speed)
    motor2.moveB(speed)
    sleep(t)


def Stop(t=0):
    motor1.stop()
    motor2.stop()
    sleep(t)


def Left(speed=100, t=0):
    motor1.moveF(speed)
    motor2.moveB(speed)
    sleep(t)


def Right(speed=100, t=0):
    motor1.moveB(speed)
    motor2.moveF(speed)
    sleep(t)
