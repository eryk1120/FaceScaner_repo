from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from json import dumps
import time
app = Flask(__name__)
api = Api(app)

todos = {
    0: 'do the shopping',
    1: 'build the codez',
    2: 'paint the door',
}

# todo tester
@app.route("/api/todo", methods=['GET'])
def give_todos():
     x = dumps(todos)
     return x+'\n'

@app.route("/api/", methods=['PUT'])
def new_todos():
        todos.pop(key, None)
        return '', status.HTTP_204_NO_CONTENT

# website tester
@app.route('/hello')
def hello():
    return """ hello world  """


@app.route('/api/skan/',methods=['GET'])
def make_skan():
    print('-----------beginning skanning')
    time.sleep(1)
    print('-----------finished skanning')
    return "DONE\n", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port =5012)

