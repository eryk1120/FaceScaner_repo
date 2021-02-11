import RPi.GPIO as GPIO
import time

cameras = {
"0":{
    "trig":40
    },
"1":{
    "trig":38
    },
"2":{
    "trig":37
    }
}

projectors = {
"0":{
    "trig":36,
    "ready":35
    },
"1":{
    "trig":33,
    "ready":32
    }
}

class head():

    def __init__(self, cams, projs):
        GPIO.setmode(GPIO.BOARD)

        self.c = cams
        self.p = projs

        for key in self.c:
            GPIO.setup(self.c[key]["trig"],GPIO.OUT)

        for key in self.p:
            GPIO.setup(self.p[key]["trig"],GPIO.OUT)
            GPIO.setup(self.p[key]["ready"],GPIO.IN, pull_up_down=GPIO.PUD_UP)

        print('done <3')

    def __del__(self):
        GPIO.cleanup()

    def RUN(self):

        # first half

        GPIO.output(self.p['1']['trig'],GPIO.HIGH)
        GPIO.output(self.p['1']['trig'],GPIO.LOW)

        if GPIO.input(self.p['0']['ready']):
            print('entered this if')
            GPIO.wait_for_edge(self.p['0']['ready'], GPIO.FALLING)

        GPIO.output(self.c['0']['trig'],GPIO.HIGH)
        GPIO.output(self.c['1']['trig'],GPIO.HIGH)

        GPIO.output(self.c['0']['trig'],GPIO.LOW)
        GPIO.output(self.c['1']['trig'],GPIO.LOW)


        # second half
        time.sleep(4)

        GPIO.output(self.p['1']['trig'],GPIO.HIGH)
        GPIO.output(self.p['1']['trig'],GPIO.LOW)

        if  GPIO.input(self.p['1']['ready']):
            print('entered this if')
            GPIO.wait_for_edge(self.p['1']['ready'], GPIO.FALLING)

        GPIO.output(self.c['0']['trig'],GPIO.HIGH)
        GPIO.output(self.c['2']['trig'],GPIO.HIGH)

        GPIO.output(self.c['0']['trig'],GPIO.LOW)
        GPIO.output(self.c['2']['trig'],GPIO.LOW)


if __name__ == "__main__":
    try:
        h = head(cameras,projectors)
        h.RUN()
        del h
    except KeyboardInterrupt:
        del h
