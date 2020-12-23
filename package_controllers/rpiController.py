import time
from gpiozero import CPUTemperature
import RPi.GPIO as GPIO

class RpiController():

    def __init__(self, _process_paramaters):
        print("Rpi: create")
        self.dev = _process_paramaters[0]
        self.repeat = _process_paramaters[1]
        self.repeat_delay = _process_paramaters[2]
        self.gpioC = _process_paramaters[4]

        self.sensor_reading = [1, 1, 1]

    def start(self):
        print("Rpi: start")
        try:
            if (self.repeat == True):
                while self.repeat:
                    self.get_readings()
                    time.sleep(self.repeat_delay)
            else:
                self.get_readings()
        except Exception as e:
            print("Rpi: error")

    def get_readings(self):
        print("Rpi: run")
        rpi_cpu = 1
        rpi_mem = 1

        self.sensor_reading = [rpi_cpu, rpi_mem, get_cpu_temp()]
        #print(temp)

    def get_cpu_temp(self):
        GPIO.setmode(GPIO.BCM)
        cpu = CPUTemperature()
        rpi_temp = cpu.temperature
        return rpi_temp

    def finish(self):
        print("Rpi: finish")
        repeat = False

    def get_sensor_reading(self):
        return self.sensor_reading
