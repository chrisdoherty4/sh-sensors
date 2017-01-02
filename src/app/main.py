'''
Created on 2 Jan 2017

@author: chrisdoherty
'''

from HubRoom import HubRoom
from config import occupied_config, unoccupied_config, red_led_pins, green_led_pins, motion_sensor_pin
from time import sleep

# Create a new hub room object
hub_room = HubRoom(motion_sensor_pin, red_led_pins, green_led_pins, unoccupied_config, occupied_config)

# Initialise and kill it when keyboard interrupt
try: 
    hub_room.change_to_unoccupied()
    
    while 1:
        sleep(0.1)
except KeyboardInterrupt:
    hub_room.stop_monitoring()