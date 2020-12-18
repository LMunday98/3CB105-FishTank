import os
import glob
import time

class TempController():

    def __init__(self, _dev, _repeat):
        self.dev = _dev
        self.repeat = _repeat

        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')

        base_dir = '/sys/bus/w1/devices/'
        device_folder = glob.glob(base_dir + '28*')[0]
        self.device_file = (device_folder + '/w1_slave')

    def start(self):
        print("Start: temp")
        try:
            if (self.repeat == True):
                while self.repeat:
                    print(self.read_temp())
                    time.sleep(5)
            else:
                print(self.read_temp())

        except Exception as e:
            print("error temp")

    def read_temp_raw(self):
        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp(self):
        lines = self.read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return temp_c, temp_f
