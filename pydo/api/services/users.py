from pydo.api.services.app import AppService

class UserService(AppService):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
    