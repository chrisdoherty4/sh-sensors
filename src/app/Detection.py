'''
Created on 23 Dec 2016

@author: chrisdoherty
'''

import time

# Represents a single detection.
class Detection():
    # start_ time of detection
    start = None
    
    # end_ time of detection
    end = None
    
    # Begins a new detection
    def start(self):
        self.start = time.time()
        
    # Ends the detection
    def stop(self):
        self.end = time.time()
      
    # Calculates the detection length in seconds.
    def detection_len(self):
        return self.end - self.start