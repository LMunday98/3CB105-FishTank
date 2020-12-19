import RPi.GPIO as GPIO

class GpioController():

    def __init__(self):
        print("GPIO: create")
        GPIO.setwarnings(False)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)

        self.gpio_in_array = []
        self.gpio_out_array = []

    def setup_gpio_in(self, gpio_pin):
        gpio_in = GPIO.setup(gpio_pin, GPIO.IN)
        self.gpio_in_array.append(gpio_in)
        #return gpio_in

    def gpio_get_input(self, gpio_pin):
        return GPIO.input(gpio_pin)

    def setup_gpio_out(self, gpio_pin, freq=None):
        gpio_out = GPIO.setup(gpio_pin, GPIO.OUT)
        gpio_out = GPIO.PWM(gpio_pin, freq)
        self.gpio_out_array.append(gpio_out)
        return gpio_out

    def finish(self):
        print("GPIO: finish")
        for gpio in self.gpio_out_array:
            gpio.stop()
        GPIO.cleanup()
