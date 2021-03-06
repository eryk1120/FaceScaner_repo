from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from json import dumps
import time
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


table = Table()
#head = Head(cams=cameras,projs=projectors)




app = Flask(__name__)
api = Api(app)




@app.route("/api", methods=['GET'])
def calibrate():
    #head.calibrate('1','1')

    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 6001        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'1:1')
        data = s.recv(1024)

    print('Received', repr(data))
            

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port =8002)