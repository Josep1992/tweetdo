from flask import Blueprint
from project.app.services.users import UserService

class UsersBlueprint(Blueprint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = UserService()