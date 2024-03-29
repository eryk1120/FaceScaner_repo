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
        "trig":38,
        "ready":40
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
        self.l = lights


        self.cam_flag = None

        print("CONSTRUCTOR")
        print(f"CREATED: {self.cam_flag}")
        
        for key in self.c:
            GPIO.setup(self.c[key]["trig"],GPIO.OUT)

        for key in self.p:
            GPIO.setup(self.p[key]["trig"],GPIO.OUT)
            GPIO.setup(self.p[key]["ready"],GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        for key in self.l:
            GPIO.setup(self.l[key]["trig"],GPIO.OUT)

        print('done <3')

        #GPIO.add_event_detect(self.p['1']["ready"], GPIO.RISING)
        #GPIO.add_event_callback(self.p['1']["ready"], self.calback)
    
    
    def calback(self,pin):
        #print("BAM!")
        #print(f"USED: {self.cam_flag}")
        #print(id(self))
        pass
        #GPIO.output(self.c[self.cam_flag]['trig'],GPIO.HIGH)
        #print(self.cam_flag)
        #GPIO.output(self.c[self.cam_flag]['trig'],GPIO.LOW)


    def listener(self,port=6000, host='127.0.0.1'):
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
                        task, proj, cams = ids.split(':')

                        print(f'given task is: {task}')

                        if task == '[S]':
                            print(f'begining task: {task}')
                            
                            t0 = time.time()

                            self.UP()
                            time.sleep(0.05)
                            self.BOT()

                            t1= time.time()
                            t = t1-t0
                            print(f"took {t} to complete sequence")

                        elif task =='[C]':
                            print(f'begining task: {task}')
                            cams = cams.split(';')
                            print(f'cams: {cams}')
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

    def UP(self):
        for _ in range(14):
            GPIO.output(self.p['0']['trig'],GPIO.HIGH)
            GPIO.output(self.p['0']['trig'],GPIO.LOW)

            GPIO.output(self.c['0']['trig'],GPIO.HIGH)
            GPIO.output(self.c['1']['trig'],GPIO.HIGH)
            GPIO.output(self.c['3']['trig'],GPIO.HIGH)
            print("XD")
            GPIO.output(self.c['0']['trig'],GPIO.LOW)
            GPIO.output(self.c['1']['trig'],GPIO.LOW)
            GPIO.output(self.c['3']['trig'],GPIO.LOW)

            time.sleep(0.04)

        GPIO.output(self.p['0']['trig'],GPIO.HIGH)
        GPIO.output(self.p['0']['trig'],GPIO.LOW)

        GPIO.output(self.l['0']['trig'],GPIO.HIGH)

        GPIO.output(self.c['0']['trig'],GPIO.HIGH)
        GPIO.output(self.c['1']['trig'],GPIO.HIGH)
        GPIO.output(self.c['3']['trig'],GPIO.HIGH)
        time.sleep(10/1000)

        GPIO.output(self.l['0']['trig'],GPIO.LOW)

        GPIO.output(self.c['0']['trig'],GPIO.LOW)
        GPIO.output(self.c['1']['trig'],GPIO.LOW)
        GPIO.output(self.c['3']['trig'],GPIO.LOW)

    def BOT(self):
        for _ in range(14):
            GPIO.output(self.p['1']['trig'],GPIO.HIGH)
            GPIO.output(self.p['1']['trig'],GPIO.LOW)

            GPIO.output(self.c['1']['trig'],GPIO.HIGH)
            GPIO.output(self.c['2']['trig'],GPIO.HIGH)
            print("XD")
            GPIO.output(self.c['1']['trig'],GPIO.LOW)
            GPIO.output(self.c['2']['trig'],GPIO.LOW)

            time.sleep(0.04)
        GPIO.output(self.p['1']['trig'],GPIO.HIGH)
        GPIO.output(self.p['1']['trig'],GPIO.LOW)

        GPIO.output(self.l['0']['trig'],GPIO.HIGH)
        GPIO.output(self.c['1']['trig'],GPIO.HIGH)
        GPIO.output(self.c['2']['trig'],GPIO.HIGH) 
        time.sleep(10/1000)
        GPIO.output(self.l['0']['trig'],GPIO.LOW)
        GPIO.output(self.c['1']['trig'],GPIO.LOW)
        GPIO.output(self.c['2']['trig'],GPIO.LOW) 



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

        print("trigger projector: %s and camera: %s" % (projektor_id, camera_id))

        print("PINS projector: %s and camera: %s" % (self.p[projektor_id]['trig'], self.c[self.cam_flag]['trig']))

        

        for _ in range(14):

            GPIO.output(self.p[projektor_id]['trig'],GPIO.HIGH)
            GPIO.output(self.p[projektor_id]['trig'],GPIO.LOW)


            #sequential camera trigerr 
            GPIO.output(self.c[self.cam_flag]['trig'],GPIO.HIGH)
            print(self.cam_flag)
            GPIO.output(self.c[self.cam_flag]['trig'],GPIO.LOW)

            time.sleep(0.04)

        GPIO.output(self.p[projektor_id]['trig'],GPIO.HIGH)
        GPIO.output(self.p[projektor_id]['trig'],GPIO.LOW)

		
        #print("here")# with flash  
        GPIO.output(self.l['0']['trig'],GPIO.HIGH)
        GPIO.output(self.c[self.cam_flag]['trig'],GPIO.HIGH)
        time.sleep(10/1000)
        GPIO.output(self.l['0']['trig'],GPIO.LOW)
        GPIO.output(self.c[self.cam_flag]['trig'],GPIO.LOW)

        
        
        

        
        

        


if __name__ == "__main__":
    try:

        h = Head(cameras,projectors)

        h.listener()
        #h.BOT()
        #time.sleep(1)
        #h.UP()

        del h

    except KeyboardInterrupt:
        del h
