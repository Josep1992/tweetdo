import os
import json
from os.path import join

from constants import CONSTANTS

database = join(CONSTANTS['ROOT'], 'db.json')

def initialize():
    # create db.json file in ./server
    if(os.path.exists(database) == False):
        with open(database,"a+") as file:
            db = {}
            db["todos"] = {}
            json.dump(db,file,indent=2,sort_keys=True)
    pass

def create_todo(payload):
    if(os.path.exists(database)):
        with open(database) as file:
            try:
                obj = json.load(file)
                obj["todos"][payload["id"]] = payload
                with open(database, "w") as f:
                    json.dump(obj,f,indent=2,sort_keys=True)
                
            except Exception as e:
                print("APPENDING TO FILE FAILED todo:{} exception: {}".format(payload["todo"],e))
            

def todos():
    response = None
    with open(database,"r") as file:
        try:
            data = json.load(file)
            response = data
        except Exception as e:
            print("CREATING TODOS RESPONSE FROM JSON FILE exception: {}".format(e))
    return response