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
repeat_delay = 1

# setup controllers

servo = ServoController(dev, repeat, repeat_delay)
tempSensor = TempController(dev, repeat, repeat_delay)
#pumpController = PumpController()

controller_array = []
controller_array.append(servo)
controller_array.append(tempSensor)

thread_controller = ThreadController(controller_array, repeat)
thread_controller.start()

if (repeat == True):
    try:
        input()
    except Exception as e:
        print("force quit")

    tempSensor.repeat = False
    servo.repeat = False

servo.finishServo()

sys.exit()
