'''
Created on 30 Dec 2016

@author: chrisdoherty
'''

from threading import Thread
from time import sleep

class UnoccupiedState(Thread):    
    # The detection container
    _detections = None
    
    # Interval to check for between detections
    _detection_interval = 10
    
    # Number of back to back detections with "interval" or less between
    # them before we trigger the next state.
    _detection_threshold = 5
    
    # The thread to keep running.
    _running = True
    
    # The number of detections currently identified with an "interval" or less between
    # them
    _detection_activation = 0
    
    # Function to call when the state is ready for change
    _occupied_callback = None
    
    def __init__(self, detection_container, detection_interval, detection_threshold, occupied_callback):
        super(UnoccupiedState, self).__init__()
        
        print "UnoccupiedState: created (detection interval=%s, detection threshold=%s)" % (detection_interval, detection_threshold)
        
        self._detections = detection_container
        self._detection_interval
        self._detection_threshold = detection_threshold
        self._occupied_callback = occupied_callback
    
    # Checking for occupied state
    def run(self):
        previous_detection = None
        current_detection = None
        
        while self._running:
            if not self._detections.empty():
                print "UnoccupiedState: processing detection"
                
                current_detection = self._detections.get()
                print current_detection
                
                # Do we have a previous detection?
                if previous_detection == None:
                    print "UnoccupiedState: first detection"
                    previous_detection = current_detection
                else:
                    
                    # Is the gap between the previous detection and this detection greater than the
                    # required interval for an increase in activation count?
                    if (current_detection.start - previous_detection.end) > self._detection_interval:
                        print "UnoccuepiedState: interval too short, resetting activation count"
                        self._detection_activation = 0
                    else:
                        print "UnoccupiedState: incrementing activation count"
                        self._detection_activation+= 1
                        
                    if self._detection_activation >= self._detection_threshold:
                        print "UnoccupiedState: activation count equal to threshold"
                        self._occupied_callback()
                    
                    previous_detection = current_detection
                
            sleep(0.5)
        
        print "UnoccupiedState: thread stopped"
                
    def stop(self):
        print "UnoccupiedState: stopping thread"
        self._running = False
            