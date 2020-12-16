# Import libraries
import RPi.GPIO as GPIO
import time

class ServoController():

    def __init__(self):
        # Set GPIO numbering mode
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)

        # Set pin 11 as an output, and define as servo1 as PWM pin
        GPIO.setup(11,GPIO.OUT)
        self.servo1 = GPIO.PWM(11,50) # pin 11 for servo1, pulse 50Hz

        # Start PWM running, with value of 0 (pulse off)
        self.servo1.start(0)



    def beginServo(self):
        # Loop to allow user to set servo angle. Try/finally allows exit
        # with execution of servo.stop and GPIO cleanup :)

        try:
            while True:
                #Ask user for angle and turn servo to it
                angle = float(input('Enter angle between 0 & 180: '))
                self.servo1.ChangeDutyCycle(2+(angle/18))
                time.sleep(0.1)
                self.servo1.ChangeDutyCycle(0)

        finally:
            #Clean things up at the end
            self.servo1.stop()
            GPIO.cleanup()
            print("Goodbye!")
