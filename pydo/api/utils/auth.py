from http import HTTPStatus
from functools import wraps
from flask import request,jsonify
from pydo.api.services.users import UserService

decode = UserService.decode

def authenticate(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        response = {
            'success': False,
            'errors': {
                'message': 'Provide a valid auth token.'
            }
        }
        authorization = request.headers.get('Authorization')
        if not authorization:
            return jsonify(response), HTTPStatus.FORBIDDEN
        token = authorization.split(' ')[1]
        decoded = decode(token)
        if "id" in decoded:
            user = UserService.get({**decoded})
            return fn(*args,**kwargs)
    return wrapper
