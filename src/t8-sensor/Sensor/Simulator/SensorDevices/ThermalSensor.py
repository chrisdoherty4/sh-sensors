from AbstractSensor import AbstractSensor

'''
ThermalSensor

This sensor currently does nothing.
'''
class ThermalSensor(AbstractSensor):
    # Constructor.
    def __init(self):
        super(ThermalSensor, self).__init__("Thermal Sensor")