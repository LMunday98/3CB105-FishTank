# Servo Control
import RPi.GPIO as GPIO
import time

class ServoController():

    def __init__(self):
        servoPIN = 14
        self.servoDelay = 0.25
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPIN, GPIO.OUT)

        self.p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
        self.p.start(7) # Initialization

    def beginServo(self):
        #self.p.ChangeDutyCycle(5)
        try:
            while True:
                userInp = input("2.5 - 12.5:\n")
                self.operateServo(userInp)
        except KeyboardInterrupt:
            p.stop()
            GPIO.cleanup()

    def operateServo(self, duration):
          self.p.ChangeDutyCycle(duration)
          time.sleep(self.servoDelay)
