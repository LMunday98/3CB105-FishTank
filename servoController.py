# Import libraries
import RPi.GPIO as GPIO
import time

class ServoController():

    def __init__(self):
        self.auto = True
        self.repeat = True
        self.delayTime = 5

        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11,GPIO.OUT)
        self.servo1 = GPIO.PWM(11,50)
        self.servo1.start(0)

    def beginServo(self):
        print("servo")

        if (self.auto == True):
            # flip
            self.moveServo(180)
            time.sleep(0.01)
            self.moveServo(180)
            time.sleep(1)

            # reset
            self.moveServo(0)
            time.sleep(0.01)
            self.moveServo(0)
            time.sleep(0.01)
        else:
            angle = float(input('Enter angle between 0 & 180: '))
            self.moveServo(angle)
            time.sleep(0.1)



    def calcMoveAngle(self, angle):
        return (2+(angle/18))

    def moveServo(self, angleToMove):
        self.servo1.ChangeDutyCycle(self.calcMoveAngle(angleToMove))
        time.sleep(0.1)
        self.servo1.ChangeDutyCycle(0)
