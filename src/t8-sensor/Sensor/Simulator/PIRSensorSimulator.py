from Sensor.Simulator.AbstractSimulator import AbstractSimulator
from Sensor.Simulator.ActivityLevel import ActivityLevel
from Sensor.Simulator.PIRSimulatorStates.LowActivityState import LowActivityState as LAS
from Sensor.Simulator.PIRSimulatorStates.MediumActivityState import MediumActivityState as MAS
from Sensor.Simulator.PIRSimulatorStates.HighActivityState import HighActivityState as HAS
from Sensor.Simulator.SensorDevices.PIRSensor import PIRSensor as PIRS

# PIR Sensor Simulator
class PIRSensorSimulator(AbstractSimulator):     
    # Constructor.
    # Creates the appropriate activity state for the sensor simulation
    # Operates using real GPIO numbers as opposed to individual pin
    # numbers
    def __init__(self, activityLevel, pin):
        super(PIRSensorSimulator, self).__init__(activityLevel)
        
        if (activityLevel == ActivityLevel.LOW):
            self._state = LAS(PIRS(pin))
        elif (activityLevel == ActivityLevel.MEDIUM):
            self._state = MAS(PIRS(pin))
        elif (activityLevel == ActivityLevel.HIGH):
            self._state = HAS(PIRS(pin))
    
    # Starts the simulation
    def start(self):
        self._state.run()
    
    # Stops the simulation
    def stop(self):
        self._state.stop()
        