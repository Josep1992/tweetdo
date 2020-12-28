from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from pydo.config import Config

app = Flask(__name__,static_folder='client')
app.config.from_object(Config)
CORS(app)

# from pydo.database import initialize
# initialize() not using the @file system anymore

# migrate to POSTGRES ---> currently using SQLite
db = SQLAlchemy(app)

from pydo.api import create_api
create_api(app)
