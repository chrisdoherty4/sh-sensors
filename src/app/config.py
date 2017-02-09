'''
Created on 2 Jan 2017

@author: chrisdoherty
'''
# For development purposes you would expect to see a high detection_interval and low 
# detection_threshold for the unoccupied_config; and a short timeout in seconds for occupied_config

# Real values are dependent on the environment and desired sensitivity

# Set development mode values
DEV_MODE = False

if not DEV_MODE:
    # Occupied state configuration
    occupied_config = {
        # Time to wait for no detections thereby assuming the room is now unoccupied
        # Seconds
        "timeout": 60*3
        }
    
    # Unoccupied state configuration
    unoccupied_config = {
        # The time between consecutive detections in seconds that contribute to the 
        # 'threshold' argument. We look for <= the interval between detections.
        "max_detection_interval": 30, 
        
        # The number of consecutive detections with the specified interval required 
        # before we assume the room is occupied
        "required_consecutive_detections": 3
        }
    
    # Represenst the hub room configuration
    hub_room_config = {
        # The pin the motion sensor is attached to.
        "sensing_pin": 4
        }

else: 
    
    # Occupied state configuration
    occupied_config = {
        # Time to wait for no detections thereby assuming the room is now unoccupied
        # Seconds
        "timeout": 10
        }
    
    # Unoccupied state configuration
    unoccupied_config = {
        # The time between consecutive detections in seconds that contribute to the 
        # 'threshold' argument. We look for <= the interval between detections.
        "max_detection_interval": 5, 
        
        # The number of consecutive detections with the specified interval required 
        # before we assume the room is occupied
        "required_consecutive_detections": 1
        }
    
    # Represenst the hub room configuration
    hub_room_config = {
        # The pin the motion sensor is attached to.
        "sensing_pin": 7
        }