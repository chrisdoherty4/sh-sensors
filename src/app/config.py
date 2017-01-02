'''
Created on 2 Jan 2017

@author: chrisdoherty
'''
# For development purposes you would expect to see a high detection_interval and low 
# detection_threshold for the unoccupied_config; and a short timeout in seconds for occupied_config

# Real values are dependent on the environment and desired sensitivity


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
    "detection_interval": 5, 
    
    # The number of consecutive detections with the specified interval required 
    # before we assume the room is occupied
    "detection_threshold": 1
    }

# An array of red LED pin numbers.
red_led_pins = [25]

# An array of green led pin numbers
green_led_pins = [9]

# The motion sensor pin 
motion_sensor_pin = 7