import os

class Config:
    PORT = os.environ.get('PORT')
    ROOT = os.path.abspath(os.path.dirname(__file__))
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:MtfJpyivabhLJAvb6LZJMDyybMocC@localhost/'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///pydo.db'