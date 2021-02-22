from flask import Flask, jsonify
from flask_restful import Resource, Api, abort, reqparse
import threading, queue
import time

from stolik import Table
from sequence_v1 import Head

app = Flask(__name__)
api = Api(app)

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




table = Table()
head = Head(cameras,projectors)

        


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
            head.RUN()
        triggerQueue.task_done()

triggerQueue = queue.Queue()
triggerWorkerThread = threading.Thread(target=triggerMessageWorker)
triggerWorkerThread.daemon = True
triggerWorkerThread.start()


#               ------- KALIBRACJA --------
def calibMessageWorker():
    while True:
        item = calibQueue.get()
        #proj_id = item[1]
        proj_id=0
        print(proj_id)
        proj_id=str(proj_id)

        cam_id =  item[2]
        print(cam_id)
        cam_id = str(cam_id)
        
        #tu wstawiony kod aktywującą sekwencję dla konkretnego projektora i kamery
        print("trigger projector: %s and camera: %s" % (proj_id, cam_id))

        head.calibrate(camera_id=cam_id,projektor_id=proj_id)

        
        
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
            messagesset.switch_with_args(message,
                               parser.parse_args()['ctrl-param-a'],
                               parser.parse_args()['ctrl-param-b'])
        else:
            messagesset.switch(message)
        return jsonify(answer="OK");



api.add_resource(hardwareServer, '/hardwareServer',
                                      '/')

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0', port= 8002)
