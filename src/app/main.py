'''
Created on 2 Jan 2017

@author: chrisdoherty
'''

from Application import Application
from threading import Thread
from time import sleep

app = Application()

Thread(target = app.hub_room_thread).start()

sleep(1)

app.run()