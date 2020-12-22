from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from pydo.database import initialize
from pydo.config import Config

app = Flask(__name__,static_folder='client')
app.config.from_object(Config)
CORS(app)
initialize()
# migrate to a @real database
# db = SQLAlchemy(app)

from pydo.api import create_api

create_api(app)