import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8,GPIO.OUT)

GPIO.setup(8,GPIO.OUT)
time.sleep(1)
GPIO.output(8,GPIO.HIGH)

GPIO.output(8,GPIO.LOW)
time.sleep(1)

GPIO.cleanup()

