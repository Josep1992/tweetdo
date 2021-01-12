from http import HTTPStatus
from functools import wraps
from flask import request,jsonify
from project.app.services.users import UserService

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
        
        try:
            decoded = decode(token)
            if "id" in decoded:
                user = UserService.get({**decoded}) # pass the user to the request
                kwargs["user"] = user
                return fn(*args,**kwargs)
        except Exception as e:
            print("EXCPETION <-------> ",e)
            status = HTTPStatus.INTERNAL_SERVER_ERROR
            resp = {
                'success': False,
                'errors': {
                    'message': 'Internal Server Error'
                },
            }
            if e.__class__.__name__ == "jwt.ExpiredSignatureError": # I think im referring to the @wrong thing
                resp["errors"]["message"] = 'Authentication token expired'
                status = HTTPStatus.UNAUTHORIZED
            return jsonify(resp), status
    return wrapper
