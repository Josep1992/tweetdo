from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from config import Config

server = Flask(__name__,static_folder='client')
server.config.from_object(Config)
CORS(server)

# from database import initialize
# initialize() not using the @file system anymore

# migrate to POSTGRES ---> currently using SQLite
db = SQLAlchemy(server)

from project.app import create_api

create_api(server)
