#sudo python Documents/3CB105-FishTank/main.py

import sys
import time
import threading

import datetime

from readTemp import ReadTemp
from pumpController import PumpController
from servoController import ServoController

# program setup

dev = False
repeat = False

servo = ServoController(dev, repeat)
tempSensor = ReadTemp(dev, repeat)
#pumpController = PumpController()

# defs

def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

# processing

start = datetime.time(23, 0, 0)
end = datetime.time(1, 0, 0)
print(time_in_range(start, end, datetime.time()))

# start multiprocessing

try:
    thread_temperature = threading.Thread(target=tempSensor.start())
    thread_servo = threading.Thread(target=servo.start())

    if (repeat == True):
        thread_temperature.setDaemon(True)
        thread_servo.setDaemon(True)

    thread_temperature.start()
    thread_servo.start()

except Exception as e:
    print("error thread")

servo.finishServo()

sys.exit()
