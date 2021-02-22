import RPi.GPIO as GPIO
import time
import stolik

    
cameras = {
    "0":{
        "trig":40
        },
    "1":{
        "trig":38
        },
    "2":{
        "trig":36
        },
    "3":{
        "trig":37
        }

    }

projectors = {
    "0":{
        "trig":10,
        "ready":8
        },
    "1":{
        "trig":33,
        "ready":32
        }
    }

class Head():


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

    def UP1(self):
        pass
    def UP2(self):
        pass
    def BOT1(self):
        pass
    def BOT2(self):
        GPIO.output(self.p['0']['trig'],GPIO.HIGH)
        GPIO.output(self.p['0']['trig'],GPIO.LOW)
        time.sleep(1)
        #GPIO.wait_for_edge(self.p['0']['ready'], GPIO.FALLING, timeout=5000)

        #GPIO.output(self.c['0']['trig'],GPIO.HIGH)
        #GPIO.output(self.c['1']['trig'],GPIO.HIGH)
        #GPIO.output(self.c['2']['trig'],GPIO.HIGH)
        #GPIO.output(self.c['3']['trig'],GPIO.HIGH)

        #time.sleep(0.001)

        #GPIO.output(self.c['0']['trig'],GPIO.LOW)
        #GPIO.output(self.c['1']['trig'],GPIO.LOW)
        #GPIO.output(self.c['2']['trig'],GPIO.LOW)
        #GPIO.output(self.c['3']['trig'],GPIO.HIGH)


    def RUN(self):

        self.BOT2()


        



    def blink(self):
        GPIO.setup(8,GPIO.OUT)
        time.sleep(1)
        GPIO.output(8,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(8,GPIO.LOW)
        time.sleep(1)

    def calibrate(self,camera_id, projektor_id):

        GPIO.output(self.p[projektor_id]['trig'],GPIO.HIGH)
        GPIO.output(self.c["0"]['trig'],GPIO.HIGH)   #1
        GPIO.output(self.c["1"]['trig'],GPIO.HIGH)   #3
        GPIO.output(self.c["2"]['trig'],GPIO.HIGH)   #2
        GPIO.output(self.c["3"]['trig'],GPIO.HIGH)   #0

        time.sleep(0.001)

        GPIO.output(self.p[projektor_id]['trig'],GPIO.LOW)
        GPIO.output(self.c["0"]['trig'],GPIO.LOW)
        GPIO.output(self.c["1"]['trig'],GPIO.LOW)
        GPIO.output(self.c["2"]['trig'],GPIO.LOW)
        GPIO.output(self.c["3"]['trig'],GPIO.LOW)



if __name__ == "__main__":
    try:
        h = Head(cameras,projectors)



        for i in range(10000000):
            print(i)
            h.calibrate("0","0")
            
            time.sleep(0.05)

            
            
            #h.RUN()

        #h.blink()

        del h
    except KeyboardInterrupt:
        del h
