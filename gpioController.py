import RPi.GPIO as GPIO

class GpioController():

    def __init__(self, _process_paramaters):
        print("GPIO: create")
        #GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        self.gpio_out_array = []

        servo = _process_paramaters[0]
        pump = _process_paramaters[1]

        self.setup_gpio_out(servo[0], servo[1])
        self.setup_gpio_in(pump[0])

    def setup_gpio_in(self, gpio_pin):
        gpio_in = GPIO.setup(gpio_pin, GPIO.IN)
        #return gpio_in

    def gpio_get_input(self, gpio_pin):
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
