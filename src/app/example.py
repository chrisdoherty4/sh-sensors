import RPi.GPIO as GPIO
import thread
import time

GPIO.setmode(GPIO.BCM)

# We're going to use pins 4 and 18 where 4 is out and 18 is in.
# 	GPIO4 	Out
#	GPIO18 	In

PIN_OUT = 4
PIN_IN = 18

GPIO.setup(PIN_OUT, GPIO.OUT)
GPIO.setup(PIN_IN, GPIO.IN)

def PinOut(threadName, delay) :
	status = False
	while True :
		status = not status
		GPIO.output(PIN_OUT, status)
		time.sleep(3)

def PinIn(threadName, delay) :
	while True :
		if (GPIO.input(PIN_IN)) :
			print "Something's moving..."
		else :
			print "Nothing there..."
		time.sleep(1)

# Start a new thread for each output and input
thread.start_new_thread(PinOut, ("Pin out", 0))
thread.start_new_thread(PinIn, ("Pin in", 0))

# Let the program run for 20 seconds.
time.sleep(20)

GPIO.cleanup()