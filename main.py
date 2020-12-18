#sudo python Documents/3CB105-FishTank/main.py

import sys
import time

from datetime import datetime, time

from tempController import TempController
from pumpController import PumpController
from servoController import ServoController
from threadController import ThreadController

# program setup

dev = False
repeat = True
repeat_delay = 3

process_paramaters = [dev, repeat, repeat_delay]
# setup controllers

servo = ServoController(process_paramaters)
tempSensor = TempController(process_paramaters)
pumpController = PumpController()

# add controllers to array

controller_array = []
controller_array.append(servo)
controller_array.append(tempSensor)

# setup threading

thread_controller = ThreadController(controller_array, repeat)
thread_controller.start()

# finish and clean up processes

if (repeat == True):
    try:
        input()
    except Exception as e:
        print("force quit")

thread_controller.finish_threads()
sys.exit()
