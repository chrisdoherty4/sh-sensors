'''
Created on 2 Jan 2017

@author: chrisdoherty
'''

# Occupied state configuration
occupied_config = {
    # Time to wait for no detections thereby assuming the room is now unoccupied
    # Seconds
    "timeout": 30
    }

# Unoccupied state configuration
unoccupied_config = {
    # The time between consecutive detections in seconds that contribute to the 
    # 'threshold' argument. We look for <= the interval between detections.
    "max_detection_interval": 30, 
    
    # The number of consecutive detections with the specified interval required 
    # before we assume the room is occupied
    "required_consecutive_detections": 1
    }

# Represenst the hub room configuration
hub_room_config = {
    # The pin the motion sensor is attached to.
    "sensing_pin": 4
    }