from datetime import datetime
from pydo.api.services.app import AppService
from pydo import db
from pydo.models.users import Users

from passlib.hash import pbkdf2_sha256 as sha256

class UserService(AppService):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

    def generate_hash(self,password):
        return sha256.hash(password)

    def verify_hash(self,password, hash):
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