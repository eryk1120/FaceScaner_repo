import RPi.GPIO as GPIO
import time

trig_in = 37
trig_out  = 40



GPIO.setmode(GPIO.BOARD)


GPIO.setup(trig_in, GPIO.OUT)



GPIO.setup(trig_out, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



print("done with init ")
cams = [11,12,13,15]
for i in [11,12,13,15]:
    print(f'camera: {i}')
    cam1 = i
    GPIO.setup(cam1, GPIO.OUT)


def calback(cha):
    pass

GPIO.add_event_detect(trig_out, GPIO.RISING)
GPIO.add_event_callback(trig_out, calback)

for _ in range(15):
    GPIO.output(trig_in,GPIO.HIGH)
    GPIO.output(trig_in,GPIO.LOW)

    GPIO.output(cams[0],GPIO.HIGH)
    GPIO.output(cams[1],GPIO.HIGH)
    GPIO.output(cams[2],GPIO.HIGH)
    GPIO.output(cams[3],GPIO.HIGH)
    print("bam")
    GPIO.output(cams[0],GPIO.LOW)
    GPIO.output(cams[1],GPIO.LOW)
    GPIO.output(cams[2],GPIO.LOW)
    GPIO.output(cams[3],GPIO.LOW)

    

    

    time.sleep(0.040)