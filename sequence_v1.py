import RPi.GPIO as GPIO
import time
import stolik
import socket

cameras = {
    "0":{
        "trig":11
        },
    "1":{
        "trig":12
        },
    "2":{
        "trig":13
        },
    "3":{
        "trig":15
        }

    }


projectors = {
    "1":{
        "trig":40,
        "ready":38
        },
    "0":{
        "trig":37,
        "ready":32
        }
    }


lights ={
    "0":{
        "trig":8,
        }
    }


class Head():




    def __init__(self, cams, projs):
        GPIO.setmode(GPIO.BOARD)

        self.c = cams
        self.p = projs

        self.cam_flag = None

        print("CONSTRUCTOR")
        print(f"CREATED: {self.cam_flag}")
        
        for key in self.c:
            GPIO.setup(self.c[key]["trig"],GPIO.OUT)

        for key in self.p:
            GPIO.setup(self.p[key]["trig"],GPIO.OUT)
            GPIO.setup(self.p[key]["ready"],GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        print('done <3')

        GPIO.add_event_detect(self.p['0']["ready"], GPIO.RISING)
        GPIO.add_event_callback(self.p['0']["ready"], self.calback)
    
    
    def calback(self,pin):
        print("BAM!")
        print(f"USED: {self.cam_flag}")
        print(id(self))

        GPIO.output(self.c[self.cam_flag]['trig'],GPIO.HIGH)
        print(self.cam_flag)
        GPIO.output(self.c[self.cam_flag]['trig'],GPIO.LOW)


    def listener(self,port=6001, host='127.0.0.1'):
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((host, port))
                s.listen()
                conn, addr = s.accept()

                with conn:
                    print('Connected by', addr)
                    while True:
                        data = conn.recv(1024)

                        if not data:
                            break

                        ids = data.decode('UTF-8')
                        proj, cams = ids.split(':')
                        cams = cams.split(';')
                        print(f'proj:{proj}')
                        t0 = time.time()
                        for cam in cams:
                            self.calibrate(cam,proj)
                        t1= time.time()
                        t = t1-t0
                        print(f"took {t} to complete sequence")
                        
                        conn.sendall(b'xDDD')
    
    
        


    


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
        time.sleep(0.005)
        GPIO.output(self.p['0']['trig'],GPIO.LOW)

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

        print('begining calibrating')
        self.cam_flag = camera_id
        print(f"CHANGED: {self.cam_flag}")

        for _ in range(15):

            GPIO.output(self.p[projektor_id]['trig'],GPIO.HIGH)
            GPIO.output(self.p[projektor_id]['trig'],GPIO.LOW)

            time.sleep(0.04)

        

        
        
        

        
        

        


if __name__ == "__main__":
    try:
        h = Head(cameras,projectors)

        h.listener()

        del h

    except KeyboardInterrupt:
        del h
