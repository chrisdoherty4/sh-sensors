# Abstract sensor.
class AbstractSensor(object):
	# A string name for this sensor.
	_name = "DEFAULT"
	
	# Constructor
	def __init__(self, name):
		self._name = name
		
	def getName(self):
		return self._name
