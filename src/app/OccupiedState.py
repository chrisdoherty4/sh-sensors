'''
Created on 30 Dec 2016

@author: chrisdoherty
'''

from threading import Timer
from datetime import datetime

class OccupiedState():
    # Timer used to determine unoccupied
    timer_ = None
    
    # Timeout for motion to class room as unoccupied
    timeout_ = 30.0
    
    # Callback when we're unoccupied
    unoccupied_callback_ = None
    
    # Are we, or aren't we handling detections?
    handle_detections_ = False
    
    # Initialises internal variables.
    def __init__(self, timeout, unoccupied_callback):
        self.timeout_ = timeout
        self.unoccupied_callback_ = unoccupied_callback
        self.debug("OccupiedState: initialised (timeout=%s)" % (timeout))
    
    # Fired when a new detection is available.
    def new_detection(self, detection):
        if self.handle_detections_:
            self.debug("OccupiedState: new detection")
            
            if self.timer_ != None:
                self.timer_.cancel()
            
            self.debug("OccupiedState: resetting timeout period")
            self.timer_ = Timer(self.timeout_, self.room_unoccupied_)
            self.timer_.start()
    
    # Stops this thread
    def cancel_timer(self):
        self.debug("OccupiedState: cancelling timer")
        self.timer_.cancel()
    
    # Stop or start the handling of detections.
    def handle_detections(self, status):
        if status == False and self.timer_ != None: 
            self.cancel_timer()
            
        self.handle_detections_ = status
    
    # Debug and callback call
    def room_unoccupied_(self):
        self.debug("OccupiedState: room unoccupied, changing state")
        self.unoccupied_callback_()
        
    def debug(self, message):
        time = datetime.time(datetime.now())
        print("[%d:%d:%d] %s" % (time.hour, time.minute, time.second, message))
        
    def __str__(self):
        return "OccupiedState"