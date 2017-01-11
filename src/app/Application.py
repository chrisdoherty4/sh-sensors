'''
Created on 11 Jan 2017

@author: chrisdoherty
'''

from time import sleep

# Represents the application as a single object.
class Application(object):
    
    # A hub room object
    hub_room_ = None

    # Initialises internal variables
    def __init__(self, hub_room):
        self.hub_room_ = hub_room
        print "Application: initialised"
    
    # Main programme loop
    def run(self):
        print "Application: running"
        self.hub_room_.start_monitoring()
        
        try:
            while 1:
                sleep(0.1)
        except KeyboardInterrupt:
            self.hub_room_.stop_monitoring()
            print "Application: stopped"
        