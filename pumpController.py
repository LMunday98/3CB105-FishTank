import time

class PumpController():

    def __init__(self, _process_paramaters, _pump_operation_params):
        print("Pump: create")
        self.dev = _process_paramaters[0]
        self.repeat = _process_paramaters[1]
        self.repeat_delay = _process_paramaters[2]
        self.gpioC = _process_paramaters[4]
        
        self.pin = _pump_operation_params[0]

        self.gpioC.setup_gpio_in(self.pin)

    def start(self):
        print("Pump: start")
        try:
            if (self.repeat == True):
                while self.repeat:
                    self.check_water()
                    time.sleep(self.repeat_delay)
            else:
                self.check_water()
        except Exception as e:
            print("Pump: error")

    def check_water(self):
        print("Pump: run")
        print(self.gpioC.gpio_get_input(self.pin))

    def finish(self):
        print("Pump: finish")
        self.repeat = False
