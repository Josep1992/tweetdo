from flask.helpers import send_file
from os.path import join

# from pydo.api.services.user import users
from pydo.api.controllers.todo import todos

blueprints = [todos]
PREFIX = "/api/v1/todos"

def create_api(app):
    
    @app.route('/', defaults={'path': ''},methods=["GET"])
    def index(path): return send_file(join(app.static_folder, 'index.html'))

    for blueprint in blueprints:
        app.register_blueprint(blueprint,url_prefix=PREFIX)