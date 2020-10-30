from datetime import date
from flask import Flask,request
from flask.helpers import send_file
from flask.json import jsonify
from uuid import uuid4
from os.path import join
import database
from database import create_todo

from constants import CONSTANTS

app = Flask(__name__,static_folder='static')
database.initialize()


@app.route('/', defaults={'path': ''},methods=["GET"])
def index(path): return send_file(join(app.static_folder, 'index.html'))


@app.route('/todos',methods=["GET"])
def todos():
    payload = database.todos()
    response = [payload["todos"][id] for id in payload["todos"]]    
    return jsonify({"todos":response})


@app.route('/add',methods=["POST"])
def add_todo():
    payload = request.get_json(request.data)

    if(payload['todo'] == ''):
        return jsonify({"error": "Todo's can't be empty"})

    payload['id'] = str(uuid4())
    payload['date'] = date.isoformat(date.today())

    create_todo(payload)

    return jsonify(payload)


if __name__ == "__main__":
    app.run(port=CONSTANTS['PORT'])