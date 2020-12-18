import os

class PumpController():

    def __init__(self):
        print("Pump: create")

    def pump_off(self):
        print("off")
        try:
            subprocess.call( "echo '1-1' |sudo tee /sys/bus/usb/drivers/usb/unbind", shell=True)
        except Exception:
            print("problem")
            pass

    def pump_on(self):
        print("on")
