from datetime import date
from uuid import uuid4
from flask import Blueprint

from pydo.database import create_todo,update_todo,clear_todos,todos,delete_todo
from pydo import app

todos = Blueprint('todos', __name__)

class TodoService():
    def __init__(self,*,**kwargs):
        super().__init__(**kwargs)

    @todos.route('/api/todos',methods=["GET"])
    def list(self):
        payload = todos()
        response = [payload["todos"][id] for id in payload["todos"]]
        return self.jsonify({"todos":response,"success":True})

# @app.route('/api/todos',methods=["GET"])
# def list():
#     payload = todos()
#     response = [payload["todos"][id] for id in payload["todos"]]
#     return jsonify({"todos":response,"success":True})


# @app.route('/api/add',methods=["POST"])
# def add_todo():
#     payload = request.get_json(request.data)

#     if payload['todo'] == '':
#         return jsonify({"error": "Pydo nothing really?!","success": False})

#     payload['id'] = str(uuid4())
#     payload['date'] = date.isoformat(date.today())

#     todo = create_todo(payload)

#     return jsonify({"todo": todo,"success":True})


# @app.route('/api/edit',methods=["PUT"])
# def edit_todo():
#     payload = request.get_json(request.data)

#     if payload['id'] == '':
#         return jsonify({"error": "id not found","success": False})

#     todo = update_todo(payload)

#     return jsonify({"todo": todo,"success":True})


# @app.route('/api/clear',methods=["DELETE"])
# def clear():
#     clear_todos()
#     return jsonify({"todos": [],"success":True})



# @app.route('/api/delete',methods=["DELETE"])
# def delete():
#     payload = request.get_json(request.data)

#     if payload['id'] == "":
#         return jsonify({"error": "id not found","success":False})

#     delete_todo(payload["id"])

#     return jsonify({"message": 'Todo Deleted', "id": payload["id"],"success":True})