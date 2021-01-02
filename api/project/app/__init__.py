from flask.helpers import send_file
from os.path import join

from project.app.controllers.users import users
from project.app.controllers.todo import todos

blueprints = [
    {"routes":todos,"prefix":"/api/v1/todos"},
    {"routes":users,"prefix":"/api/v1/users"}
]

def create_api(server):
    
    @server.route('/', defaults={'path': ''},methods=["GET"])
    # I have to make this route catch all unhandled request and send them to the client
    # index.html 
    def index(path): return send_file(join(server.static_folder, 'index.html'))

    for blueprint in blueprints:
        server.register_blueprint(blueprint["routes"],url_prefix=blueprint["prefix"])