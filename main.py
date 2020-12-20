# sudo python Documents/3CB105-FishTank/main.py
# cd Documents/3CB105-FishTank
# sudo python main.py

import sys

from config import Config
from threadController import ThreadController

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

# import config file
config = Config()
repeat = config.get_param_settings()[1]
gpioC = config.get_param_settings()[4]

# setup process controllers
controller_servo = ServoController(config.get_param_settings(), config.get_param_servo())
controller_temperature = TempController(config.get_param_settings())
contorller_pump = PumpController(config.get_param_settings(), config.get_param_pump())

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
