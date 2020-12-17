from flask import Blueprint
from pydo.models.users import Users

users = Blueprint("users",__name__)
class UserService:
    def __init__(self):
        pass