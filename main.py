import sys
from readTemp import ReadTemp
from pumpController import PumpController
from servoController import ServoController
from time import sleep

#pumpController = PumpController()
#pumpController.pump_off()
#sleep(3)
#pumpController.pump_on()

servo = ServoController()
servo.beginServo()

tempSensor = ReadTemp()
tempSensor.begin_monitoring()
