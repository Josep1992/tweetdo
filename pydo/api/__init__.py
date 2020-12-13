from flask import request
from flask.json import jsonify

from pydo.api.services.user import User
from pydo.api.services.todo import Todo

def create_api(app):
    # don't know if this is correct
    Todo(app,request,jsonify)