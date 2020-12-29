from pydo.api.services.app import AppService
from pydo import db
from pydo.models.users import Users
from pydo.config import Config

from passlib.hash import pbkdf2_sha256 as sha256

import jwt

class UserService(AppService):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def encode_JWT(data):
        return jwt.encode({**data,**Config.EXPIRATION},Config.SECRET,algorithm="HS256")

    @staticmethod
    def decode(token):
        return jwt.decode(token,Config.SECRET,algorithms=["HS256"])

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

    def verify_email_already_exist(self,data):
        user = Users.query.filter_by(email=data["email"]).first()
        if(user):
            return {"message": "Email already exist"}

    def create(self,data):
        user = Users(email=data["email"],password=data["password"])
        
        db.session.add(user)
        db.session.commit()

        return user.to_object

    def get(self,data):
        user = Users.query.filter_by(email=data["email"]).first()
        if not user:
            return None

        return user.to_object