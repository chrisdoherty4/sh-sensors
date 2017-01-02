'''
Created on 30 Dec 2016

@author: chrisdoherty
'''

from threading import Timer
from time import sleep

class OccupiedState():
    # Timer used to determine unoccupied
    _timer = None
    
    # Timeout for motion to class room as unoccupied
    _timeout = 30.0
    
    # Callback when we're unoccupied
    _unoccupied_callback = None
    
    # Status of thread
    _running = True
    
    def __init__(self, timeout, unoccupied_callback):
        self._timeout = timeout
        self._unoccupied_callback = unoccupied_callback
        print "OccupiedState: created (timeout=%s)" % (timeout)
    
    def motion_detected(self):
        print "OccupiedState: motion detected, resetting timer"
        
        if self._timer != None:
            self._timer.cancel()
            
        self._timer = Timer(self._timeout, self._unoccupied_callback)
        self._timer.start()
    
    # Stops this thread
    def stop(self):
        print "OccupiedState: stopping"
        self._timer.cancel()
        self._running = False