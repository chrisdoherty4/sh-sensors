from Sensor.Simulator.PIRSimulatorStates.AbstractSimulationState import AbstractSimulationState as ASS

# High activity for PIR Sensor Simulator
class HighActivityState(ASS):
    # Sets up values for a high activity simulation.
    def __init__(self, sensor):
        super(HighActivityState, self).__init__(sensor, 0, 3, 2, 5)