'''
Created on 11 Jan 2017

@author: chrisdoherty
'''

from HubRoom import HubRoom 
from Display import Display
from time import sleep
from config import hub_room_config, unoccupied_config, occupied_config

# Represents the application as a single object.
class Application(object):
    
    # A hub room object
    hub_room_ = None
    
    # Display
    display_ = None

    # Initialises internal variables
    def __init__(self):
        print("Application: initialised")
    
    # Main programme loop
    def run(self):
        print("Application: running")
        self.display_ = Display()
        self.hub_room_.register_observer(self.display_)
        self.display_.mainloop()
    
    # SHould be run in its own thread
    def hub_room_thread(self):
        self.hub_room_ = HubRoom(hub_room_config, unoccupied_config, occupied_config)
        self.hub_room_.start_monitoring()
        
        try:
            while 1:
                sleep(0.1)
        except KeyboardInterrupt:
            self.hub_room_.stop_monitoring()
            print("Application: stopped")
        
        
        