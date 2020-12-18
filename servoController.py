# Import libraries
import RPi.GPIO as GPIO
import time

class ServoController():

    def __init__(self, _process_paramaters, _opTime):
        print("Servo: create")
        self.dev = _process_paramaters[0]
        self.repeat = _process_paramaters[1]
        self.repeat_delay = _process_paramaters[2]
        self.timeC = _process_paramaters[3]
        self.opTime = _opTime

        GPIO.setwarnings(False)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11,GPIO.OUT)
        self.servo1 = GPIO.PWM(11,50)
        self.servo1.start(0)

    def start(self):
        print("Servo: start")
        try:
            if (self.repeat == True):
                while self.repeat:
                    self.runServo()
                    time.sleep(self.repeat_delay)
            else:
                self.checkTime()
        except Exception as e:
            print("Servo: error")

    def checkTime(self):
        is_between_time = self.timeC.is_time_between(self.opTime[0], self.opTime[1])
        if (is_between_time):
            self.runServo()

    def runServo(self):
        print("Servo: run")
        if (self.dev == True):
            print("Servo: dev movement")
        else:
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

    def finish(self):
        print("Servo: finish")
        self.moveServo(0)
        self.repeat = False
        self.servo1.stop()
        GPIO.cleanup()

    def calcMoveAngle(self, angle):
        return (2+(angle/18))

    def moveServo(self, angleToMove):
        self.servo1.ChangeDutyCycle(self.calcMoveAngle(angleToMove))
        time.sleep(0.1)
        self.servo1.ChangeDutyCycle(0)
