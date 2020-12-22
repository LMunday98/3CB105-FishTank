# sudo python Documents/3CB105-FishTank/main.py
# cd Documents/3CB105-FishTank
# sudo python main.py

import sys
sys.dont_write_bytecode = True

from config import Config
from package.threadController import ThreadController

from package.tempController import TempController
from package.pumpController import PumpController
from package.servoController import ServoController

# import config file
config = Config()

# setup process controllers
controller_servo = ServoController(config.get_program_settings(), config.get_param_servo())
controller_temperature = TempController(config.get_program_settings())
contorller_pump = PumpController(config.get_program_settings(), config.get_param_pump())

# add controllers to array
controller_array = []
controller_array.append(controller_servo)
controller_array.append(controller_temperature)
controller_array.append(contorller_pump)

# setup threading
thread_controller = ThreadController(controller_array, config.get_program_settings())
thread_controller.start()

# finish and clean up threads
thread_controller.finish_threads()

# exit program
sys.exit()
