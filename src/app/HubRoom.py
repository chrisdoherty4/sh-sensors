'''
Created on 8 Jan 2017

@author: chrisdoherty
'''

from DetectionManager import DetectionManager
from UnoccupiedState import UnoccupiedState
from OccupiedState import OccupiedState
from gpiozero import MotionSensor

class HubRoom():
    # Container for tracking the detections
    detection_manager_ = None
    
    # The current state of the hub room: occupied/unoccupied
    state_ = None
    
    # Config for unoccupied state
    unoccupied_state_config_ = None
    
    # Config for occupied state
    occupied_state_config_ = None
    
    # Hub room configuration 
    hub_room_config_ = None
    
    # Initialise the hub room into an unoccupied state.
    def __init__(self, hub_room_config, unoccupied_state_config, occupied_state_config):
        # Internal variables
        self.hub_room_config_ = hub_room_config
        self.unoccupied_state_config_ = unoccupied_state_config
        self.occupied_state_config_ = occupied_state_config
        
        # Create objects.
        self.state_ = self.create_unoccupied_state_()
        self.detection_manager_ = DetectionManager(MotionSensor(hub_room_config['sensing_pin']))
    
    # Begins the process of monitoring activity in the hub room
    def start_monitoring(self):
        self.state_.handle_detections(True)
    
    # Stops activity monitoring of the hub room.
    def stop_monitoring(self):
        self.state_.handle_detections(False)
        self.state_ = self.create_unoccupied_state_()
    
    # Callback triggered when the room becomes occupied
    def occupied(self):
        self.state_.handle_detections(False)
        self.state_ = self.create_occupied_state_()
        self.state_.handle_detections(True)
    
    # Callback triggered when ther oom becomes unoccupied.
    def unoccupied(self):
        self.state_.handle_detections(False)
        self.state_ = self.create_unoccupied_state_()
        self.state_.handle_detections(True)
        
    # Creates a new occupied state object
    def create_occupied_state_(self):
        state = OccupiedState(self.occupied_state_config_['timeout'], self.unoccupied)
        self.detection_manager_.new_detection = state.new_detection
        return state
    
    # Creates a new unoccupied state object.
    def create_unoccupied_state_(self):
        state = UnoccupiedState(self.unoccupied_state_config['max_detection_interval'], self.unoccupied_state_config['required_consecutive_detections'], self.occupied)
        self.detection_manager_.new_detection = state.new_detection
        return state
    
    