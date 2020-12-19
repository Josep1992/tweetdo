from datetime import date
from uuid import uuid4

from pydo.database import todos,create_todo,update_todo,clear_todos,delete_todo
from pydo.api.services.app import AppService

class TodoService(AppService):
    def __init__(self):
        pass

    def list(self):
        data = todos()
        return  [data["todos"][id] for id in data["todos"]]

    def update(self,data):
        return update_todo({**data})

    def delete_all(self):
        clear_todos()
        return []

    def delete(self,id):
        delete_todo(id)

    def create(self,data):
        return create_todo({
            **data,
            'id':  str(uuid4()),
            'date': date.isoformat(date.today())
        })

