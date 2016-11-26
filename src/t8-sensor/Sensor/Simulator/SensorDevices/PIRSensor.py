from AbstractSensor import AbstractSensor
import RPi.GPIO as GPIO

# PIRSensor representing a real PIR Sensor
class PIRSensor(AbstractSensor) :
	
	# The Pin this PIRSensor will act on.
	_pin = -1
	
	# Constructor
	#
	# Sets up the GPIO pin for out usage.
	# @param pin The GPIO pin number to use.
	def __init__ (self, pin) :
		super(PIRSensor, self).__init__("PIR Sensor")
		
		self._pin = pin
		
		GPIO.setup(pin, GPIO.OUT)
	
	# Turn the sensor on.
	def on(self):
		GPIO.output(self._pin, True)
		
	# Turn the sensor off.
	def off(self):
		GPIO.output(self._pin, False)
		
		
		