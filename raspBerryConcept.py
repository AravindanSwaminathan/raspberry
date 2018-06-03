#Not Tested
#03-06-2018
#vkku

import RPi.GPIO as GPIO
import time
PIN = 11
SLEEP_TIME = 5

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pin,GPIO.OUT)
count = 0
while True:
	print "led on"
	GPIO.output(PIN, GPIO.HIGH)
	time.sleep(SLEEP_TIME)
	print "led off"
	GPIO.output(PIN, GPIO.LOW)
	time.sleep(1)
	count += 1
	print "I blinked " , count , "times"
	if count > 5:
		print "Too much blinking !"
		break
	else:
		print "Still not tired !"
