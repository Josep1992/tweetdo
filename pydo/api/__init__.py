from pydo.api.services.user import users
from pydo.api.services.todo import todos

blueprints = [todos,users]

def create_api(app):
    for blueprint in blueprints:
        app.register_blueprint(blueprint,url_prefix="/api")