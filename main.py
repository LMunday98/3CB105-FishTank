#sudo python Documents/3CB105-FishTank/main.py

import sys
import threading
import time

from readTemp import ReadTemp
from pumpController import PumpController
from servoController import ServoController

# program setup

servo = ServoController()
tempSensor = ReadTemp()
#pumpController = PumpController()

# setup multiprocessing

def temperatureLoop():
    try:
        tempSensor.begin_monitoring()
    except Exception as e:
        print("error temp")

def servoLoop():
    try:
        servo.start()
    except Exception as e:
        print("error servo")

# start multiprocessing

try:

    thread_temperature = threading.Thread(target=temperatureLoop)
    #thread_temperature.setDaemon(True)
    thread_temperature.start()

    thread_servo = threading.Thread(target=servoLoop)
    thread_servo.setDaemon(True)
    thread_servo.start()

except Exception as e:
    print("error thread")

if (servo.repeat == True):
    try:
        input()
        print("exit")

    except Exception as e:
        print("force exit")

sys.exit()
