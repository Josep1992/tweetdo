from project import db
from project.models.users import Users
from config import Config

from datetime import datetime
from passlib.hash import pbkdf2_sha256 as sha256
import jwt


class UserService:
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
        user = self.get(data)
        if(user):
            return {"message": "Email already exist"}

    def create(self,data):
        user = Users(email=data["email"],password=data["password"])
        print(user)
        db.session.add(user)
        db.session.commit()

        return user.to_object

    def update(self,data):
        user = self.get(data,to_object=False)
        
        user.email = data["email"]
        user.password = data["password"]
        user.date_updated = datetime.utcnow()

        db.session.commit()

        return self.get(data).to_object

    @staticmethod
    def get(data,to_object=True):
        print("DATA",data["email"])
        user = Users.query.filter_by(email=data["email"]).first()
        print(user)
        if not user:
            return None

        if to_object == True:
            return user.to_object
        return user