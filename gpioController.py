import os
import glob
import RPi.GPIO as GPIO

class GpioController():

    def __init__(self):
        print("GPIO: create")
        #GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        self.gpio_out_array = []
        self.device_file = self.setup_bus_slave()

    def setup_gpio_in(self, gpio_pin):
        gpio_in = GPIO.setup(gpio_pin, GPIO.IN)
        #return gpio_in

    def get_sensor_input(self, gpio_pin):
        return GPIO.input(gpio_pin)

    def setup_gpio_out(self, gpio_pin, freq=None):
        GPIO.setup(gpio_pin, GPIO.OUT)
        servo = GPIO.PWM(gpio_pin,freq)
        servo.start(0)
        return servo

    def finish(self):
        print("GPIO: finish")
        for gpio in self.gpio_out_array:
            gpio.stop()
        GPIO.cleanup()

    def setup_bus_slave(self):
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')

        base_dir = '/sys/bus/w1/devices/'
        device_folder = glob.glob(base_dir + '28*')[0]
        return (device_folder + '/w1_slave')

    def read_raw_bus_data(self):
        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def get_bus_input(self):
        lines = self.read_raw_bus_data()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0)
            lines = read_raw_bus_data()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c
