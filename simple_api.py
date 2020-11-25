from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from json import dumps

app = Flask(__name__)
api = Api(app)

todos = {'0':'xD'}

class TodoSimple(Resource):
     def get(self, todo_id):
          return {todo_id: todos[todo_id]}

     def put(self, todo_id):
          print ("data aquired")
          print (todo_id)
          todos[todo_id] = request.form['data']
          return {todo_id: todos[todo_id]}

@app.route('/hello')
def hello():
    return 'Hello, World'

api.add_resource(TodoSimple, '/api/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True, port =5012)