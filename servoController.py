# Import libraries
import RPi.GPIO as GPIO
import time

class ServoController():

    def __init__(self, _dev, _repeat):
        self.dev = _dev
        self.repeat = _repeat
        self.autoMove = True
        self.delayTime = 5

        #GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11,GPIO.OUT)
        self.servo1 = GPIO.PWM(11,50)
        self.servo1.start(0)

    def start(self):
        print("servo")
        try:
            if (self.repeat == True):
                while True:
                    self.runServo()
                    time.sleep(5)
            else:
                self.runServo()
        except Exception as e:
            print("error servo")

    def runServo(self):
        if (self.dev == True):
            print("servo dev movement")
        else:
            if (self.autoMove == True):
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
            elif (self.autoMove == False):
                angle = float(input('Enter angle between 0 & 180: '))
                self.moveServo(angle)
                time.sleep(0.1)

    def finishServo(self):
        self.servo1.stop()
        GPIO.cleanup()

    def calcMoveAngle(self, angle):
        return (2+(angle/18))

    def moveServo(self, angleToMove):
        self.servo1.ChangeDutyCycle(self.calcMoveAngle(angleToMove))
        time.sleep(0.1)
        self.servo1.ChangeDutyCycle(0)
