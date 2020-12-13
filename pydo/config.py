import os

class Config:
    PORT = os.environ.get('PORT')
    ROOT = os.path.abspath(os.path.dirname(__file__))
    PYDO = 'sqlite:///pydo.db'