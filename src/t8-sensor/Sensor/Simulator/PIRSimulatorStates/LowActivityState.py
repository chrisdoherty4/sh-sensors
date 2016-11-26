from Sensor.Simulator.PIRSimulatorStates.AbstractSimulationState import AbstractSimulationState as ASS

# Low activity for PIR Sensor Simulator
class LowActivityState(ASS):
    # Sets up values for a high activity simulation.
    def __init__(self, sensor):
        super(LowActivityState, self).__init__(sensor, 3, 10, 0, 2)