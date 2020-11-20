from datetime import date
from flask import Flask,request
from flask.helpers import send_file
from flask.json import jsonify
from uuid import uuid4
from os.path import join
from flask_cors import CORS

import database
from database import create_todo,update_todo,clear_todos

from constants import CONSTANTS

app = Flask(__name__,static_folder='client')
CORS(app)
database.initialize()


@app.route('/', defaults={'path': ''},methods=["GET"])
def index(path): return send_file(join(app.static_folder, 'index.html'))


@app.route('/api/todos',methods=["GET"])
def todos():
    payload = database.todos()
    response = [payload["todos"][id] for id in payload["todos"]]
    return jsonify({"todos":response,"success":True})


@app.route('/api/add',methods=["POST"])
def add_todo():
    payload = request.get_json(request.data)

    if payload['todo'] == '':
        return jsonify({"error": "Pydo nothing really?!","success": False})

    payload['id'] = str(uuid4())
    payload['date'] = date.isoformat(date.today())

    todo = create_todo(payload)

    return jsonify({"todo": todo,"success":True})


@app.route('/api/edit',methods=["PUT"])
def edit_todo():
    payload = request.get_json(request.data)

    if payload['id'] == '':
        return jsonify({"error": "id not found","success": False})

    todo = update_todo(payload)

    return jsonify({"todo": todo,"success":True})


@app.route('/api/clear',methods=["DELETE"])
def clear():
    clear_todos()
    return jsonify({"todos": [],"success":True})



@app.route('/api/delete',methods=["DELETE"])
def delete_todo():
    payload = request.get_json(request.data)

    if payload['id'] == "":
        return jsonify({"error": "id not found","success":False})

    database.delete_todo(payload["id"])

    return jsonify({"message": 'Todo Deleted', "id": payload["id"],"success":True})


if __name__ == "__main__":
    app.run(port=CONSTANTS['PORT'],host="0.0.0.0")