from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from flask.helpers import send_file
from os.path import join

from config import Config

APP = Flask(__name__,static_folder='client')
APP.config.from_object(Config)
CORS(APP)

# from database import initialize
# initialize() not using the @file system anymore

# migrate to POSTGRES ---> currently using SQLite
db = SQLAlchemy(APP)

from project.app.controllers.users import users
from project.app.controllers.todo import todos

blueprints = [
    {"routes":todos,"prefix":"/api/v1/todos"},
    {"routes":users,"prefix":"/api/v1/users"}
]

@APP.route('/', defaults={'path': ''},methods=["GET"])
# I have to make this route catch all unhandled request and send them to the client
# index.html 
def entry(path): return send_file(join(APP.static_folder, 'index.html'))

for blueprint in blueprints:
    APP.register_blueprint(blueprint["routes"],url_prefix=blueprint["prefix"])
