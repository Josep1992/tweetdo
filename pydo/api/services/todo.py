from datetime import date
from uuid import uuid4

from pydo.database import update_todo,clear_todos,delete_todo
from pydo.api.services.app import AppService
from pydo import db
from pydo.models.todo import Todo

class TodoService(AppService):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

    def list(self):
        todos = Todo.query.all()
        return  [todo.to_json() for todo in todos]

    def update(self,data):
        return update_todo({**data})

    def delete_all(self):
        clear_todos()
        return []

    def delete(self,id):
        delete_todo(id)

    def create(self,data):
        todo = Todo(todo=data["todo"],completed=data["checked"])

        db.session.add(todo)
        db.session.commit()

        return todo.to_json()

