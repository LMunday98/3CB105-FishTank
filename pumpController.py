import os

class PumpController():

    def __init__(self, _process_paramaters):
        print("Pump: create")
        self.dev = _process_paramaters[0]
        self.repeat = _process_paramaters[1]
        self.repeat_delay = _process_paramaters[2]
        gpioC = _process_paramaters[4]

        self.lvlSensor = gpioC.setup_gpio_in(8)

    def start(self):
        print("Pump: start")

    def finish(self):
        print("Pump: finish")
