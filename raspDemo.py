import RPi.GPIO as GPIO
import time
pin=11
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pin,GPIO.OUT)
count = 0
while True:
	print "led on"
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(5)
	print "led off"
	GPIO.output(pin,GPIO.LOW)
	time.sleep(1)
	count += 1
	print "I blinked " , count , "times"
	if count > 5:
		print "Too much blinking !"
		break
	else:
		print "Still not tired !"

