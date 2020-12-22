
import time

class TempController():

    def __init__(self, _process_paramaters):
        print("Temp: create")
        self.dev = _process_paramaters[0]
        self.repeat = _process_paramaters[1]
        self.repeat_delay = _process_paramaters[2]
        self.gpioC = _process_paramaters[4]

        self.sensor_reading = 0

    def start(self):
        print("Temp: start")
        try:
            if (self.repeat == True):
                while self.repeat:
                    self.read_temp()
                    time.sleep(self.repeat_delay)
            else:
                self.read_temp()
        except Exception as e:
            print("Temp: error")

    def read_temp(self):
        print("Temp: run")
        temp = self.gpioC.get_bus_input()
        self.sensor_reading = temp
        print(temp)

    def finish(self):
        print("Temp: finish")
        repeat = False

    def get_sensor_reading(self):
        return self.sensor_reading
