#sudo python Documents/3CB105-FishTank/main.py

import sys
import time
from datetime import datetime, time

from threadController import ThreadController
from timeController import TimeController
from gpioController import GpioController

from tempController import TempController
from pumpController import PumpController
from servoController import ServoController

# defs
def finish_threads():
    if (repeat == True):
        try:
            input()
        except Exception as e:
            print("*Force Quit*")

    thread_controller.finish_threads()
    gpioC.finish()

# setup operation controllers
timeC = TimeController()
gpioC = GpioController()

# program setup
dev = False
repeat = True
repeat_delay = 3
process_paramaters = [dev, repeat, repeat_delay, timeC, gpioC]

# servo operation paramters
gpio_pin = 11
freq = 50
servo_operation_times = [time(10,30), time(21,30)]
servo_operation_params = [gpio_pin, freq, servo_operation_times]

# setup process controllers
controller_servo = ServoController(process_paramaters, servo_operation_params)
controller_temperature = TempController(process_paramaters)
contorller_pump = PumpController(process_paramaters)

# add controllers to array
controller_array = []
controller_array.append(controller_servo)
controller_array.append(controller_temperature)
controller_array.append(contorller_pump)

# setup threading
thread_controller = ThreadController(controller_array, repeat)
thread_controller.start()

# finish and clean up threads
finish_threads()

# exit program
sys.exit()
