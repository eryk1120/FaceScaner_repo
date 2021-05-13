import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

GPIO.setup(8,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

print("starting")
time.sleep(1)




GPIO.output(8,GPIO.HIGH)
GPIO.output(12,GPIO.HIGH)
time.sleep(10/1000)
GPIO.output(8,GPIO.LOW)
GPIO.output(12,GPIO.LOW)
print(10)
time.sleep(3)


GPIO.cleanup()