from Sensor.Simulator.SensorDevices.PIRSensor import PIRSensor as PIRS
from time import sleep
from random import randrange

# Abstract simulation state. Handles actual simulation logic, i.e. pulses 
# for the PIR Sensor.
class AbstractSimulationState(object):
    # Maximum interval length
    _maxIntervalLen = 10
    
    # Minimum interval length
    _minIntervalLen = 0
    
    # Max length a detection can last.
    _maxDetectionLen = 10
    
    # Min length a detection can last.
    _minDetectionLen = 1
    
    # A reference to the sensor
    _sensor = ""
    
    # Determines if we're active or not.
    _active = True
    
    # The amount fo multiply each time by so we can get decimal values.
    MULTIPLYER = 100
    
    # Sets internal values and ensures the sensor is of the correct type. 
    # All times are specified in seconds.
    def __init__(self, sensor, minIntervalLen, maxIntervalLen, minDetectionLen, maxDetectionLen):
        self._maxIntervalLen = maxIntervalLen * self.MULTIPLYER
        self._minIntervalLen = minIntervalLen * self.MULTIPLYER
        self._minDetectionLen = minDetectionLen * self.MULTIPLYER
        self._maxDetectionLen = maxDetectionLen * self.MULTIPLYER
        
        if (not isinstance(sensor, PIRS)):
            raise ValueError('Incorrect type of sensor')
        else:
            self._sensor = sensor
        
    # Stops the simulation
    def stop(self):
        self._active = False
        
    # Defines the method called to run the simulation.
    def run(self):
        # Initially sleep a bit.
        sleep(self._getIntervalLen())
        
        # While active, turn the sensor on and wait X amount before turning it off and waiting
        # another X amount of time specified by the detection and interval ranges
        while self._active:
            self._sensor.on()
            sleep(self._getDetectionLen())
            self._sensor.off()
            sleep(self._getIntervalLen())
        
    # Generate a new random detection length
    def _getDetectionLen(self):
        return randrange(self._minDetectionLen, self._maxDetectionLen) / self.MULTIPLYER
    
    # Generate a new random interval length.
    def _getIntervalLen(self):
        return randrange(self._minIntervalLen, self._maxIntervalLen) / self.MULTIPLYER
        