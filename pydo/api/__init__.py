from flask.helpers import send_file
from os.path import join

# from pydo.api.services.user import users
from pydo.api.controllers.todo import todos

todos_blueprints = [todos]
TODOS_PREFIX = "/api/v1/todos"

USER_PREFIX = "/api/v1/user"

def create_api(app):
    
    @app.route('/', defaults={'path': ''},methods=["GET"])
    def index(path): return send_file(join(app.static_folder, 'index.html'))

    for blueprint in todos_blueprints:
        app.register_blueprint(blueprint,url_prefix=TODOS_PREFIX)