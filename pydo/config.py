import os

class Config:
    PORT = os.environ.get('PORT')
    ROOT = os.path.abspath(os.path.dirname(__file__)),
    SECRET = 'MtfJMDyybMocCpyivabhDd4BTV998EJazZFtJAKRLJAvb6LZJ'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///pydo.db'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:MtfJpyivabhLJAvb6LZJMDyybMocC@localhost/'