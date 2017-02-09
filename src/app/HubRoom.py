'''
Created on 8 Jan 2017

@author: chrisdoherty
'''

from DetectionManager import DetectionManager
from UnoccupiedState import UnoccupiedState
from OccupiedState import OccupiedState
from gpiozero import MotionSensor
from Display import Display
from datetime import datetime
from time import sleep

class HubRoom(object):
    # Container for tracking the detections
    detection_manager_ = None
    
    sensor_ = None
    
    # The current state of the hub room: occupied/unoccupied
    state_ = None
    
    # Config for unoccupied state
    unoccupied_state_config_ = None
    
    # Config for occupied state
    occupied_state_config_ = None
    
    # Hub room configuration 
    hub_room_config_ = None
    
    # A set of observer objects
    observers_ = set([]) 
    
    # Initialise the hub room into an unoccupied state.
    def __init__(self, hub_room_config, unoccupied_state_config, occupied_state_config):        
        # Internal variables
        self.hub_room_config_ = hub_room_config
        self.unoccupied_state_config_ = unoccupied_state_config
        self.occupied_state_config_ = occupied_state_config
        
        # Create objects.
        self.sensor_ = MotionSensor(self.hub_room_config_['sensing_pin'])
        self.detection_manager_ = DetectionManager()
        self.sensor_.when_motion = self.detection_manager_.start_detection
        self.sensor_.when_no_motion = self.detection_manager_.stop_detection
              
    
    # registers a new observer with this object
    def register_observer(self, observer):
        self.observers_.add(observer)
    
    # Begins the process of monitoring activity in the hub room
    def start_monitoring(self):
        self.debug("HubRoom: starting monitoring")
        self.state_ = self.create_unoccupied_state_()
        self.state_.handle_detections(True)
    
    # Stops activity monitoring of the hub room.
    def stop_monitoring(self):
        self.debug("HubRoom: stopping monitoring")
        self.state_.handle_detections(False)
    
    # Callback triggered when the room becomes occupied
    def occupied(self):
        self.debug("HubRoom: changing to occupied")
        self.state_.handle_detections(False)
        self.state_ = self.create_occupied_state_()
        self.state_.handle_detections(True)
        self.notify_observers()
    
    # Callback triggered when ther oom becomes unoccupied.
    def unoccupied(self):
        self.debug("HubRoom: changing to unoccupied")
        self.state_.handle_detections(False)
        self.state_ = self.create_unoccupied_state_()
        self.state_.handle_detections(True)
        self.notify_observers()
        
    # Creates a new occupied state object
    def create_occupied_state_(self):
        state = OccupiedState(self.occupied_state_config_['timeout'], self.unoccupied)
        self.detection_manager_.new_detection = state.new_detection
        return state
    
    # Creates a new unoccupied state object.
    def create_unoccupied_state_(self):
        state = UnoccupiedState(self.unoccupied_state_config_['max_detection_interval'], 
                                self.unoccupied_state_config_['required_consecutive_detections'], 
                                self.occupied)
        self.detection_manager_.new_detection = state.new_detection
        return state
    
    def notify_observers(self):
        for observer in self.observers_:
            observer.notify(self)
            
    def debug(self, message):
        time = datetime.time(datetime.now())
        print("[%d:%d:%d] %s" % (time.hour, time.minute, time.second, message))
    