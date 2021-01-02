from flask.json import jsonify
from flask import request
from project.app.blueprints.users import UsersBlueprint

users = UsersBlueprint('users', __name__)

@users.route('/',methods=["POST"])
def sign_up():
    payload = request.get_json()
    errors = {}

    if not "email" in payload or payload["email"] == "":
        errors["email"] = "Email is a required field"
    if not "password" in payload or payload["password"] == "":
        errors["password"] = "Password is a required field"

    user_already_exist = users.service.verify_email_already_exist(payload)
    if user_already_exist:
        errors["user_already_exist"] = user_already_exist["message"]

    if errors:
        return jsonify({"errors":errors,'success': False})

    payload["password"] = users.service.generate_hash(payload["password"])

    user = users.service.create(payload)

    return jsonify({"user": user, "success": True})


@users.route('/login',methods=["POST"])
def sign_in():
    payload = request.get_json()
    errors = {}

    if not "email" in payload or payload["email"] == "":
        errors["email"] = "Email is a required field"
    if not "password" in payload or payload["password"] == "":
        errors["password"] = "Password is a required field"
    
    if errors:
        return jsonify({"errors":errors,'success': False})

    user = users.service.get(payload)

    if user is None:
        errors["user_not_exist"] = "User doesn't exist"
        return jsonify({"errors":errors,'success': False})

    is_match = users.service.verify_hash(payload["password"],user["password"])

    if not is_match:
        errors["invalid_password"] = "Incorrect Password"
        return jsonify({"errors":errors,'success': False})

    token = users.service.encode_JWT({"id":user["id"],"email":user["email"]})
    user["token"] = token
    del user["password"]
    return jsonify({"user":user,'success': True})

    
