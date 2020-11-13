import os

CONSTANTS = {
    'PORT': os.environ.get('PORT'),
    'ROOT': os.path.abspath(os.path.dirname(__file__))
}