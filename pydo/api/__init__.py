from flask.helpers import send_file
from os.path import join

from pydo.api.controllers.users import users
from pydo.api.controllers.todo import todos

blueprints = [
    {"routes":todos,"prefix":"/api/v1/todos"},
    {"routes":users,"prefix":"/api/v1/users"}
]

def create_api(app):
    
    @app.route('/', defaults={'path': ''},methods=["GET"])
    def index(path): return send_file(join(app.static_folder, 'index.html'))

    for blueprint in blueprints:
        app.register_blueprint(blueprint["routes"],url_prefix=blueprint["prefix"])