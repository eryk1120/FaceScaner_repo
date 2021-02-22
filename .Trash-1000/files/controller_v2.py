import RPi.GPIO as GPIO
import time


def blink():
    GPIO.setup(36,GPIO.OUT)
    GPIO.setup(37,GPIO.OUT)
    GPIO.setup(38,GPIO.OUT)
    GPIO.setup(40,GPIO.OUT)

    for i in range(1000000):
        print(i)
        GPIO.output(40,GPIO.HIGH)
        GPIO.output(38,GPIO.HIGH)
        GPIO.output(37,GPIO.HIGH)
        GPIO.output(36,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(40,GPIO.LOW)
        GPIO.output(38,GPIO.LOW)
        GPIO.output(37,GPIO.LOW)
        GPIO.output(36,GPIO.LOW)
        time.sleep(0.4)
def button():
    GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.wait_for_edge(40, GPIO.FALLING)
    print("Button pressed!")


if __name__=="__main__":
    GPIO.setmode(GPIO.BOARD)
    button()

    GPIO.cleanup()
