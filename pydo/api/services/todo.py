from datetime import datetime
from pydo.api.services.app import AppService
from pydo import db
from pydo.models.todo import Todo

class TodoService(AppService):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

    def list(self,user_id):
        todos = Todo.query.filter_by(user_id=user_id).all()
        return  [todo.to_object for todo in todos]

    def update(self,data):
        t = Todo.query.filter_by(id=int(data["id"])).first()
        
        # t.todo = data["todo"] have to implement changing @todo value
        t.completed = data["checked"]
        t.date_updated = datetime.utcnow()

        db.session.commit()

        updated = Todo.query.filter_by(id=t.id).first()

        return updated.to_object

    def delete_all(self):
        todos = Todo.query.all()

        for todo in todos:
            db.session.delete(todo)
            db.session.commit()

        return []

    def delete(self,id):
        todo = Todo.query.filter_by(id=id).first()
        
        db.session.delete(todo)
        db.session.commit()

        return todo.to_object

    def create(self,data):
        todo = Todo(todo=data["todo"],completed=data["checked"],user_id=data["user"]["id"])
        db.session.add(todo)
        db.session.commit()

        return todo.to_object

