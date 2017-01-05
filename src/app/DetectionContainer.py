'''
Created on 23 Dec 2016

@author: chrisdoherty
'''

from Queue import Queue
from Detection import Detection
from threading import Lock

class DetectionContainer(Queue):
    # the current detection
    _detection = None
    
    # Lock to stop the detection from restarting.
    _lock = Lock()
    
    def start_detection(self):
        print "DetectionContainer: start detection"
        self._lock.acquire()
        self._detection = Detection()
        self._detection.begin()
        
    def stop_detection(self):
        if self._detection != None:
            print "DetectionContainer: stop detection"
            self._detection.end()
            self.put(self._detection)
            self._detection = None
            self._lock.release()