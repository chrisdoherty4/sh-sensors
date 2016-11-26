from Sensor.Simulator.PIRSimulatorStates.AbstractSimulationState import AbstractSimulationState as ASS

# Medium activity for PIR Sensor Simulator
class MediumActivityState(ASS):
    # Sets up values for a high activity simulation.
    def __init__(self, sensor):
        super(MediumActivityState, self).__init__(sensor, 0, 5, 1, 4)