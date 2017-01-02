'''
Created on 23 Dec 2016

@author: chrisdoherty
'''

import time

class Detection():
    # Start time of detection
    start = None
    
    # End time of detection
    end = None
    
    def begin(self):
        self.start = time.time()
        
    def end(self):
        self.end = time.time()
      
    def detection_len(self):
        return self.end - self.start