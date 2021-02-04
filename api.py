#!/usr/bin/env python
# coding=utf-8

# przykladowy fragment aplikacji siecowej sterującej ruchem stolika w lewo i zatrzymania go

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_api import status

import json
from stolik import Table

class my_resource(Resource):

    def __init__(self):
        self.known_tasks = ['RotLeft',"STOP"]

        self.table = Table() # inicjalizacja obiektu sterującego
        # inne obiekty reprezentujące

    def __del__(self):
        del self.table


    def put(self):
        data = request.get_json()
        print('got request')
        try:
            task = data['task']
            print("task: {0}".format(task))
        except:
            return status.HTTP_501_NOT_IMPLEMENTED, "error while parsing given task"

        if task not in self.known_tasks:
            return status.HTTP_501_NOT_IMPLEMENTED, "unknown task given"

        if task == "RotLeft":
            self.table.rot_letf()

        elif task=="STOP":
            self.table.stop()


        return status.HTTP_202_ACCEPTED,"done with taks: {}".format(task)

app = Flask(__name__)
api = Api(app)

api.add_resource(my_resource, '/api')


@app.route('/hello')
def hello():
    return """ hello world  """

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True, port =5012)



# przykładowa komenda CURL do weryfikacji działania programu
# w terminalu bash:
# curl -X PUT -H "Content-Type: application/json" -d '{"task":"RotLeft"}' http://localhost:5012/api
# curl -X PUT -H "Content-Type: application/json" -d '{"task":"STOP"}' http://localhost:5012/api
# curl -X PUT -H "Content-Type: application/json" -d '{"task":"WrongTask"}' http://localhost:5012/api

# w razie problemu: odwiedzenie strony http://localhost:5012/hello
# w dowolnej przeglądarce internetowej w celu sprawdzenia połączenia
