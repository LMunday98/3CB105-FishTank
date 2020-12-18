#sudo python Documents/3CB105-FishTank/main.py

import sys
import time

from threadController import ThreadController
from timeController import TimeController
from tempController import TempController
from pumpController import PumpController
from servoController import ServoController

# defs
def finishProgram():
    if (repeat == True):
        try:
            input()
        except Exception as e:
            print("*Force Quit*")

    thread_controller.finish_threads()
    sys.exit()

# program setup
dev = True
repeat = False
repeat_delay = 3
timeC = TimeController()
process_paramaters = [dev, repeat, repeat_delay, timeC]

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
finishProgram()
