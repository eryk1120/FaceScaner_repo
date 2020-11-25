from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from json import dumps

app = Flask(__name__)
api = Api(app)

todos = {
    0: 'do the shopping',
    1: 'build the codez',
    2: 'paint the door',
}


@app.route("/api/<int:key>/", methods=['GET'])
def give_todos():
     x = dumps(todos)
     return x

@app.route("/api/", methods=['PUT'])
def new_todos():
        notes.pop(key, None)
        return '', status.HTTP_204_NO_CONTENT


@app.route('/hello')
def hello():
    return 'Hello, World'


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port =5012)

