import json
from flask.json import jsonify
from flask import request
from project.app.blueprints.todo import TodoBluePrint
from project.app.utils.auth import authenticate

todos = TodoBluePrint('todos', __name__)

@todos.route('/',methods=["GET"])
@authenticate
def handle_all(**kwargs):
    user_id = kwargs["user"]["id"]
    response = todos.service.list(user_id)
    return jsonify({"todos":response,"success":True})


@todos.route('/add',methods=["POST"])
@authenticate
def create(**kwargs):
    payload = request.get_json()
    if payload['todo'] == '':
            return jsonify({"error": "Pydo nothing really?!","success": False})
            
    response = todos.service.create({**payload,'user':{**kwargs["user"]}})
    return jsonify({"todo": response,"success":True})


@todos.route('/edit',methods=["PUT"])
@authenticate
def update(**kwargs):
    payload = request.get_json()

    if payload['id'] == '':
        return jsonify({"error": "id not found","success": False})

    response = todos.service.update(payload)

    return jsonify({"todo": response,"success":True})


@todos.route('/clear',methods=["DELETE"])
@authenticate
def clear(**kwargs):
    payload = request.get_json()
    response = todos.service.delete_all({**payload,'user':{**kwargs["user"]}})
    return jsonify({"todos": response,"success":True})


@todos.route('/delete',methods=["DELETE"])
@authenticate
def delete(**kwargs):
    payload = request.get_json()

    if payload['id'] == "":
        return jsonify({"error": "id not found","success":False})

    deleted = todos.service.delete(payload['id'])

    return jsonify({"message": 'Todo Deleted', "id": payload["id"],"success":True,'todo':deleted })