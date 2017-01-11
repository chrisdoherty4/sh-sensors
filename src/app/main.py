'''
Created on 2 Jan 2017

@author: chrisdoherty
'''

from HubRoom import HubRoom
from Application import Application
from config import hub_room_config, unoccupied_config, occupied_config

# Create a new hub room object
app = Application(HubRoom(hub_room_config, unoccupied_config, occupied_config))
app.run()