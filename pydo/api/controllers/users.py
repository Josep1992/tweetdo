from flask.json import jsonify
from flask import request
from pydo.api.blueprints.users import UsersBlueprint

users = UsersBlueprint('users', __name__)

@users.route('/create',methods=["POST"])
def create_user():
    payload = request.get_json(request.data)
    errors = {}

    if not "email" in payload or payload["email"] is "":
        errors["email"] = "Email is a required field"
    if not "password" in payload or payload["password"] is "":
        errors["password"] = "Password is a required field"

    if errors:
        return jsonify({"errors":errors,'success': False})
