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
repeat_delay = 1

servo = ServoController(dev, repeat, repeat_delay)
tempSensor = TempController(dev, repeat, repeat_delay)
#pumpController = PumpController()

# defs

def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def create_thread(targetProcess):
    threads.append(threading.Thread(target=start_process, args=(targetProcess,)))

def start_process(process):
    process.start()

# processing
start = datetime.time(23, 0, 0)
end = datetime.time(1, 0, 0)
#print(time_in_range(start, end, datetime.time()))

# start multithreading

try:
    # create threads
    print("Threading: create")
    threads = []
    create_thread(tempSensor)
    create_thread(servo)

    # set daemon if repeat
    print("Threading: daemon")
    if (repeat == True):
        for t in threads:
            t.setDaemon(True)

    # start threads
    print("Threading: start")
    for t in threads:
        t.start()

except Exception as e:
    print("Threading: error")

if (repeat == True):
    try:
        input()
    except Exception as e:
        print("force quit")

    tempSensor.repeat = False
    servo.repeat = False

servo.finishServo()

sys.exit()
