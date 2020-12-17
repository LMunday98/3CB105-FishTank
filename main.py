#sudo python Documents/3CB105-FishTank/main.py

import sys
import threading
from time import sleep

from readTemp import ReadTemp
from pumpController import PumpController
from servoController import ServoController

# program setup

global run
run = True

servo = ServoController()
tempSensor = ReadTemp()
#pumpController = PumpController()

# setup multiprocessing

def temperatureLoop():
    try:
        while True:
            tempSensor.begin_monitoring()
    except Exception as e:
        print("error temp")

def servoLoop():
    try:
        while True:
            servo.beginServo()
            if (servo.repeat == False):
                break
            sleep(servo.delayTime)
    except Exception as e:
        print("error servo")
    #finally:
        #self.servo1.stop()
        #GPIO.cleanup()

# start multiprocessing

try:

    thread_temperature = threading.Thread(target=temperatureLoop)
    thread_temperature.setDaemon(True)
    thread_temperature.start()

    thread_servo = threading.Thread(target=servoLoop)
    thread_servo.daemon = True
    thread_servo.start()

except Exception as e:
    print("error thread")

try:
    input()
    print("exit")

except Exception as e:
    print("force exit")

sys.exit()
