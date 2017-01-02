'''
Created on 30 Dec 2016

@author: chrisdoherty
'''
from gpiozero import MotionSensor, LED
from UnoccupiedState import UnoccupiedState
from OccupiedState import OccupiedState
from DetectionContainer import DetectionContainer

class HubRoom():
    
    # The detections container
    detections_container = None
    
    # The PIR sensor
    sensor = None
    
    # An array of red LEDS
    red_leds = []
    
    # An array of green LEDs
    green_leds = []
    
    # The state of the room, occupied or unoccupied
    state = None
    
    # Configuration for the unoccupied state object
    unoccupied_config = None 
    
    # Configuration for the occupied state object
    occupied_config = None 
    
    # Status of the hub room monitoring
    monitoring = True
    
    def __init__(self, sensor_pin, red_led_pins, green_led_pins, unoccupied_config = {"detection_interval": 3, "detection_threshold": 5}, occupied_config = {"timeout": 60}):
        self.unoccupied_config = unoccupied_config
        self.occupied_config = occupied_config
        
        self.detections_container = DetectionContainer()
        
        # Hook up motion sensor with detections container so we can create new detections
        # autonomously
        self.sensor = MotionSensor(pin = sensor_pin, queue_len = 10)
        
        for pin in red_led_pins:
            self.red_leds.append(LED(pin))
        
        for pin in green_led_pins:
            self.green_leds.append(LED(pin))
        
        print "HubRoom: created"
        
    # Safely close down other threads
    def stop_monitoring(self):
        self.monitoring = False
        self.state.stop() 
    
    # Callback for when the unoccupied room changes to occupied
    def change_to_occupied(self):
        if not self.monitoring:
            return
        
        print "HubRoom: changing to occupied state"
        
        self.sensor.when_motion = None
        self.sensor.when_no_motion = None
        
        if self.state != None:
            self.state.stop()
        
        self.state = OccupiedState(self.occupied_config['timeout'], self.change_to_unoccupied)
        self.sensor.when_motion = self.state.motion_detected
        
        self.toggle_leds(self.green_leds, False)
        self.toggle_leds(self.red_leds, True)
    
    # Callback for when the occupied room changes to unoccupied
    def change_to_unoccupied(self):
        if not self.monitoring:
            return
        
        print "HubRoom: changing to unoccupied state"
        
        if self.state != None:
            self.state.stop()
        
        self.state = UnoccupiedState(self.detections_container, self.unoccupied_config['detection_interval'], self.unoccupied_config['detection_threshold'], self.change_to_occupied)
        self.state.start()
        
        self.sensor.when_motion = self.detections_container.start_detection 
        self.sensor.when_no_motion = self.detections_container.stop_detection
        
        self.toggle_leds(self.red_leds, False)
        self.toggle_leds(self.green_leds, True)
    
    # Toggles LEDs to the specified state
    def toggle_leds(self, leds, state):
        for led in leds:
            if state != led.is_lit:
                led.toggle()
            
