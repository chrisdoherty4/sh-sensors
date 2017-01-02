from time import sleep
from threading import Timer
from gpiozero import MotionSensor, LED
from signal import pause
            
sensor = MotionSensor(pin=7, queue_len=10)
red_led = LED(25)
green_led = LED(9)
green_led.on()
timer = None

def no_motion():
    red_led.off()
    green_led.on()

while True:
    if sensor.motion_detected:
        if timer != None:
            timer.cancel()
        
        timer = Timer(30.0, no_motion)
        timer.start()
        
        green_led.off()
        red_led.on()