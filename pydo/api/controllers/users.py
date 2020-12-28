from flask.json import jsonify
from flask import request
from pydo.api.blueprints.users import UsersBlueprint

users = UsersBlueprint('users', __name__)

@users.route('/',methods=["POST"])
def create_user():
    payload = request.get_json(request.data)
    errors = {}

    if not "email" in payload or payload["email"] == "":
        errors["email"] = "Email is a required field"
    if not "password" in payload or payload["password"] == "":
        errors["password"] = "Password is a required field"

    # user_already_exist = users.service.verify_email_already_exist(payload)
    # if user_already_exist:
    #     errors["user_already_exist"] = user_already_exist["message"]

    if errors:
        return jsonify({"errors":errors,'success': False})

    payload["password"] = users.service.generate_hash(payload["password"])

    user = users.service.create(payload)

    return jsonify({"user": user, "success": True})
