#sudo python Documents/3CB105-FishTank/main.py

import sys
import time
import threading

import datetime

from tempController import TempController
from pumpController import PumpController
from servoController import ServoController

# program setup

dev = False
repeat = True

servo = ServoController(dev, repeat)
tempSensor = TempController(dev, repeat)
#pumpController = PumpController()

# defs

def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def tempT():
    tempSensor.start()

def servoT():
    servo.start()


# processing

start = datetime.time(23, 0, 0)
end = datetime.time(1, 0, 0)
#print(time_in_range(start, end, datetime.time()))

# start multithreading

try:
    # create threads

    print("Theading: create")

    thread_temperature = threading.Thread(target=tempT)
    thread_servo = threading.Thread(target=servoT)

    # set daemon if repeat

    print("Theading: daemon")

    if (repeat == True):
        thread_temperature.setDaemon(True)
        thread_servo.setDaemon(True)

    # start threads

    print("Theading: start")

    thread_temperature.start()
    thread_servo.start()

except Exception as e:
    print("error thread")

if (repeat == True):
    try:
        input()
    except Exception as e:
        print("force quit")

    tempSensor.repeat = False
    servo.repeat = False

servo.finishServo()

sys.exit()
