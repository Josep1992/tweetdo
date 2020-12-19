from flask import Blueprint
from pydo.api.services.todo import TodoService

class TodoBluePrint(Blueprint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = TodoService()