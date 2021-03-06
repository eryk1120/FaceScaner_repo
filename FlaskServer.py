from flask import Flask, jsonify
from flask_restful import Resource, Api, abort, reqparse
import threading, queue
import time
import sys
import socket 

from stolik import Table
from sequence_v1 import Head

#sys.setcheckinterval(5)


#[11,12,13,15]
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
        "trig":37,
        "ready":40
        },
    "0":{
        "trig":29,
        "ready":32
        }
    }


lights ={
    "0":{
        "trig":8,
        }
    }

print('camera pins:', cameras)
print('projector pins', projectors)
print('lights pins',lights)


#table = Table()
#head = Head(cams=cameras,projs=projectors)


app = Flask(__name__)
api = Api(app)




        


parser = reqparse.RequestParser()
parser.add_argument('message', type=str, required=True)
parser.add_argument('ctrl-param-a', type=int, required=False)
parser.add_argument('ctrl-param-b', type=int, required=False)

class liftClass:
    def __init__(self):
        self.state = "stop"
        self.active = [0];
        self.interval = 1 #czas jednej iteracji podtrzymania
        internalEvent = threading.Event()
        internalEvent.clear()
        def internalloop():
            while True:
                if(self.active[0] > 0):
                    while not internalEvent.wait(self.interval):
                            self.active[0] = self.active[0]  -1;
                            if self.active[0] == 0:
                                self.changeState("stop");
                                break;

        loopThread = threading.Thread(target=internalloop)
        loopThread.daemon = True
        loopThread.start()

    def changeState(self, newState):
        if self.state != newState:
            if newState == "stop":
                self.state = "stop"
                self.active[0] = 0;
                print( "stop")
            if newState == "up":
                self.state = "up"
                self.active[0] = 2;
                print( "up")
            if newState == "down":
                self.state = "down"
                self.active[0] = 2;
                print( "down")
        else:
            if newState != "stop":
                self.active[0] = self.active[0] + 1;
                if self.active[0]  > 2: #zapas na dwa cykle
                    self.active[0] = 2;

liftObject = liftClass();    


#               ------- PODNOŚNIK --------
def liftMessageWorker():

    while True:
        item = liftQueue.get()
        if item == "systemup":
            liftObject.changeState("up")
            #stopMovementUp.clear();
        if item == "systemdown":
            liftObject.changeState("down")
        liftQueue.task_done()

liftQueue = queue.Queue()
liftWorkerThread = threading.Thread(target=liftMessageWorker)
liftWorkerThread.daemon = True
liftWorkerThread.start()


#               ------- KAMERY --------
def triggerMessageWorker():
    while True:

        item = triggerQueue.get()
        print(item)
        #tu wstawiony kod4
        if item == "camegatrigger":
            #head.RUN()
            pass
        triggerQueue.task_done()

triggerQueue = queue.Queue()
triggerWorkerThread = threading.Thread(target=triggerMessageWorker)
triggerWorkerThread.daemon = True
triggerWorkerThread.start()


#               ------- KALIBRACJA --------



def ask_calibrate():
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 6001        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'1:1')
        data = s.recv(1024)

    print('Received', repr(data))

def calibMessageWorker():
    while True:
        item = calibQueue.get()
        proj_id = item[1]
        
        proj_id=str(proj_id)

        cam_id =  item[2]
        
        
        cam_id = str(cam_id)
        
        #tu wstawiony kod aktywującą sekwencję dla konkretnego projektora i kamery
        print("trigger projector: %s and camera: %s" % (proj_id, cam_id))
        t0 = time.time()
        
        #head.calibrate(camera_id=cam_id,projektor_id=proj_id)
        ask_calibrate()           

        t1=time.time()
        t = t1-t0
        print(f"took {t} to complete sequence")
        
        calibQueue.task_done()

calibQueue = queue.Queue()
calibWorkerThread = threading.Thread(target=calibMessageWorker)
calibWorkerThread.daemon = True
calibWorkerThread.start()



#               ------- STOLIK --------
class stageClass:
    def __init__(self):
        self.state = "stop"
        self.active = [0];
        self.interval = 1 #czas jednej iteracji podtrzymania
        internalEvent = threading.Event()
        internalEvent.clear()
        def internalloop():
            while True:
                if(self.active[0] > 0 and ( self.state == "right" or self.state == "left")):
                    while not internalEvent.wait(self.interval):
                        self.active[0] = self.active[0]  -1
                        if self.active[0] == 0:
                            self.changeState("stop")
                            break

        loopThread = threading.Thread(target=internalloop)
        loopThread.daemon = True
        loopThread.start()

    def changeState(self, newState):
        if self.state != newState or  newState == "nextpos":
            if newState == "stop":
                self.state = "stop"
                self.active[0] = 0;
                print( "stop")
            if newState == "right":
                table.rot_right()
                self.state = "right"
                self.active[0] = 2;
                print( "right xDDDDDDDDD")
            if newState == "left":
                table.rot_letf()
                self.state = "left"
                self.active[0] = 2;
                print( "left")
            if newState == "nextpos":
                self.state = "nextpos"
                self.active[0] = 0;
                table.rot_right()
                print( "nextpos")
                print("nextpos")


        else:
            if newState != "stop":
                self.active[0] = self.active[0] + 1;
                if self.active[0]  > 2: #zapas na dwa cykle
                    self.active[0] = 2;

stageObject = stageClass(); 


def stageMessageWorker():
    while True:
        item = stageQueue.get()
        if item == "chairlefths" or item == "chairleftls":
            stageObject.changeState("left")
        if item == "chairrighths" or item == "chairrightls":
            stageObject.changeState("right")
        if item == "movenextpos":
            stageObject.changeState("nextpos")
        stageQueue.task_done()

stageQueue = queue.Queue()
stageWorkerThread = threading.Thread(target=stageMessageWorker)
stageWorkerThread.daemon = True
stageWorkerThread.start()

def restMessageWorker():
    while True:
        item = restQueue.get()
        if len(item)== 3:
            messagesset.switch_with_args(item[0], item[1], item[2])
        else:
            messagesset.switch(item[0])
        restQueue.task_done()


restQueue = queue.Queue()
restWorkerThread = threading.Thread(target=restMessageWorker)
restWorkerThread.daemon = True
restWorkerThread.start()


#      ------- PRZETWARZANIE KOMUNIKATÓW --------
class messagesset:
    @staticmethod
    def switch( message):
        if message == "systemup":
            return messagesset.systemup();
        if message == "systemdown":
            return messagesset.systemdown();
        if message == "camegatrigger":
            return messagesset.camegatrigger();
        if message == "chairlefths":
            return messagesset.chairlefths();
        if message == "chairrighths":  
            return messagesset.chairrighths();
        if message == "chairleftls":
            return messagesset.chairleftls();
        if message == "chairrightls":
            return messagesset.chairrightls();
        if message == "movenextpos":  
            return messagesset.movenextpos();
        return;

    @staticmethod
    def systemup():
        liftQueue.put("systemup")
        liftQueue.join() 
        return;

    @staticmethod
    def systemdown():
        liftQueue.put("systemdown")
        liftQueue.join() 
        return;

    @staticmethod
    def camegatrigger():
        triggerQueue.put("camegatrigger")
        triggerQueue.join() 

        return;

    @staticmethod
    def chairlefths():
        stageQueue.put("chairlefths")
        stageQueue.join() 
        return;

    @staticmethod
    def chairrighths():
        stageQueue.put("chairrighths")
        stageQueue.join() 
        return;

    @staticmethod
    def chairleftls():
        stageQueue.put("chairleftls")
        stageQueue.join() 
        return;

    @staticmethod
    def movenextpos():
        stageQueue.put("movenextpos")
        stageQueue.join() 
        return;

    @staticmethod
    def switch_with_args( message, param_a, param_b):
        if message == "calibratetrigger":
            return messagesset.calibratetrigger(param_a, param_b);

    @staticmethod
    def calibratetrigger(param_a, param_b):
        calibQueue.put(["calibratetrigger", param_a, param_b])
        calibQueue.join() 
        return;

    @staticmethod
    def chairrighths():
        stageQueue.put("chairrighths")
        stageQueue.join()
        return;

class hardwareServer(Resource):
    def get(self):
        return 'OK"'

    def post(self):
        message = parser.parse_args()['message']
        if 'ctrl-param-a' in parser.parse_args() and parser.parse_args()['ctrl-param-a'] != None:
            restQueue.put([message, parser.parse_args()['ctrl-param-a'],
                               parser.parse_args()['ctrl-param-b']])
            print(message, parser.parse_args()['ctrl-param-a'],
                               parser.parse_args()['ctrl-param-b'])
        else:
            restQueue.put([message])
        return jsonify(answer="OK");


api.add_resource(hardwareServer, '/hardwareServer',
                                      '/')

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0', port= 8002)
    #restQueue.put(["calibratetrigger",1,1])
    #for _ in range(100):
        #head.calibrate('0','0')



'''

curl -X POST http://biom1.local:8002/hardwareServer -H "Content-Type:application/json"  -d '{"message": "calibratetrigger",  "ctrl-param-a" : "0" ,  "ctrl-param-b" : "1" }'



'''