import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.IN)

buzzer=15
GPIO.setup(buzzer,GPIO.OUT)

while True:
	i=GPIO.input(11)
	if i==0:
		print "No bike",i
		GPIO.output(3,0)
		GPIO.output(7,1)
		GPIO.output(buzzer,GPIO.LOW)
		time.sleep(0.1)
	elif i==1:
		print "Bike detected",i
		GPIO.output(3,1)
		GPIO.output(7,0)
		GPIO.output(buzzer,GPIO.HIGH)
		time.sleep(0.1)