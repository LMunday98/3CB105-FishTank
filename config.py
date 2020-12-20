from datetime import datetime, time
from timeController import TimeController
from gpioController import GpioController

class Config():

    def __init__(self):
        print("Config: import")
        self.servo_operation_params = self.servo_setup()
        self.pump_operation_params = self.pump_setup()
        self.process_paramaters = self.program_setup()

    def program_setup(self):
        # program run settings
        dev = False
        repeat = False
        repeat_delay = 3
        return [dev, repeat, repeat_delay, TimeController(), self.gpio_setup()]

    def gpio_setup(self):
        gpioC = GpioController()
        gpioC.setup_gpio_out(self.servo_operation_params[0], self.servo_operation_params[1])
        gpioC.setup_gpio_in(self.pump_operation_params[0])
        return gpioC

    def servo_setup(self):
        # servo operation paramters
        servo_gpio_pin = 11
        servo_freq = 50
        servo_operation_times = [time(10,30), time(22,30)]
        return [servo_gpio_pin, servo_freq, servo_operation_times]

    def pump_setup(self):
        # pump operation paramters
        pump_gpio_pin = 8
        return [pump_gpio_pin]

    def get_param_settings(self):
        return self.process_paramaters

    def get_param_servo(self):
        return self.servo_operation_params

    def get_param_pump(self):
        return self.servo_operation_params
