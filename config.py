from datetime import datetime, time


from timeController import TimeController
from gpioController import GpioController

class Config():

    def __init__(self):
        print("Config: setup")

        # setup operation controllers
        timeC = TimeController()
        gpioC = GpioController()

        # program setup
        dev = False
        repeat = False
        repeat_delay = 3
        self.process_paramaters = [dev, repeat, repeat_delay, timeC, gpioC]

        # servo operation paramters
        servo_gpio_pin = 11
        servo_freq = 50
        servo_operation_times = [time(10,30), time(21,30)]
        self.servo_operation_params = [servo_gpio_pin, servo_freq, servo_operation_times]

        # pump operation paramters
        pump_gpio_pin = 8
        self.pump_operation_params = [pump_gpio_pin]

    def get_param_process(self):
        return self.process_paramaters

    def get_param_servo(self):
        return self.servo_operation_params

    def get_param_pump(self):
        return self.servo_operation_params
