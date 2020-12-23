# sudo python Documents/3CB105-FishTank/main.py
# cd Documents/3CB105-FishTank
# sudo python main.py

import sys
sys.dont_write_bytecode = True

from db import Db
from config import Config
from package_controllers.threadController import ThreadController

from package_controllers.tempController import TempController
from package_controllers.pumpController import PumpController
from package_controllers.servoController import ServoController

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

# insert data to mysql database
timeC = config.get_program_settings()[3]
data = [0, controller_temperature.get_sensor_reading(), contorller_pump.get_sensor_reading(), 1, 1, 1, timeC.get_current_date(), timeC.get_current_time()]
db = Db()
db.insert_data(data)

# exit program
sys.exit()
