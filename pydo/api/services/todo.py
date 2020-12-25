import datetime

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
        t = Todo.query.filter_by(id=int(data["id"])).first()
        # t["todo"] = data["todo"] have to implement changing @todo value
        t["completed"] = data["checked"]
        t["date_updated"] = datetime.utcnow()

        db.session.commit()

        updated = Todo.query.filter_by(id=t["id"]).first()

        return updated.to_json()

    def delete_all(self):
        # todos = Todo.query.all()

        # for t in todos:
        #     todo = t.to_json()
        #     print("TODO",todo)
        #     db.session.delete(int(todo["id"]))
        #     db.session.commit()

        return []

    def delete(self,id):
        deleted = Todo.query.filter_by(id=id).first()
        db.session.delete(id)
        db.session.commit()

        return deleted.to_json()

    def create(self,data):
        todo = Todo(todo=data["todo"],completed=data["checked"])

        db.session.add(todo)
        db.session.commit()

        return todo.to_json()

