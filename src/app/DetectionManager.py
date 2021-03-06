'''
Created on 23 Dec 2016

@author: chrisdoherty
'''

from Detection import Detection
from threading import Lock

# Manages new detections using the MotionSensor.
class DetectionManager():
    # the current detection
    _detection = None
    
    # Lock to stop the detection from restarting.
    _lock = Lock()
    
    # Used when a detection finishes. Should accept 1 argument - the detection.
    new_detection = None
    
    # Initialises internal variables.
    def __init__(self):
        print("DetectionManager: initialised")
    
    # Begins a new detection based on the MotionSensor object.
    def start_detection(self):
        print("DetectionManager: start detection")
        self._lock.acquire()
        self._detection = Detection()
        self._detection.start()
        self._detection.stop()
        
        if self.new_detection != None:
            self.new_detection(self._detection)
	
        self._detection = None
        self._lock.release()
        print("DetectionManager: start deteciton function finished")
    
    # Ends a detection and passes it to the specified callback
    def stop_detection(self):
        print("DetectionManager: detection ended")
