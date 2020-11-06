import os

CONSTANTS = {
    'PORT': os.environ.get('PORT', 8080),
    'ROOT': os.path.abspath(os.path.dirname(__file__))
}