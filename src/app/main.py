from Sensor.Simulator.PIRSensorSimulator import PIRSensorSimulator
from Sensor.Simulator.ActivityLevel import ActivityLevel
from time import sleep
from thread import start_new_thread
from threading import Thread
import RPi.GPIO as GPIO

print("Setting up board")

# Ensure we set the board as BCM mode so the pin is picked up correctly.   
GPIO.setmode(GPIO.BCM)

print("Creating new PIR Simulator...")

# Create a medium activity PIR Sensor Simulator
simulator = PIRSensorSimulator(ActivityLevel.MEDIUM, 4)

print("Wrapping simulator in thread...")

start_new_thread(simulator.start, ())

class PresenceDetector(Thread):
    active = True
    _pin = 18
    def run(self):
        GPIO.setup(self._pin, GPIO.IN)
        while self.active :
            if (GPIO.input(self._pin)) :
                print "Something's moving..."
            else :
                print "Nothing there..."
            sleep(0.5)

# Start a new thread for each output and input
detector = PresenceDetector()
detector.start()

sleep(20)

print("Stopping simulator...")

simulator.stop()
detector.active = False

print("Cleaning up...")

GPIO.cleanup()

print("Exiting...")

