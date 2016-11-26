# Abstract simulator to house common variables.
class AbstractSimulator(object):
    
    # Defines the activity level for this simulator.
    _activityLevel = ""
    
    def __init__(self, activityLevel):
        self._activityLevel = activityLevel
        