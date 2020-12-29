import json
from flask.json import jsonify
from flask import request
from pydo.api.blueprints.todo import TodoBluePrint

from pydo.api.utils.auth import authenticate

todos = TodoBluePrint('todos', __name__)

@todos.route('/',methods=["GET"])
def handle_todos():
    response = todos.service.list()
    return jsonify({"todos":response,"success":True})


@todos.route('/add',methods=["POST"])
@authenticate
def create():
    payload = request.get_json(request.data)
    if payload['todo'] == '':
            return jsonify({"error": "Pydo nothing really?!","success": False})
            
    response = todos.service.create(payload)
    return jsonify({"todo": response,"success":True})


@todos.route('/edit',methods=["PUT"])
@authenticate
def update():
    payload = request.get_json(request.data)

    if payload['id'] == '':
        return jsonify({"error": "id not found","success": False})

    response = todos.service.update(payload)

    return jsonify({"todo": response,"success":True})


@todos.route('/clear',methods=["DELETE"])
@authenticate
def clear():
    response = todos.service.delete_all()
    return jsonify({"todos": response,"success":True})


@todos.route('/delete',methods=["DELETE"])
@authenticate
def delete():
    payload = request.get_json(request.data)

    if payload['id'] == "":
        return jsonify({"error": "id not found","success":False})

    deleted = todos.service.delete(payload['id'])

    return jsonify({"message": 'Todo Deleted', "id": payload["id"],"success":True,'todo':deleted })