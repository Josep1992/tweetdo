import os
import json
from os.path import join

from constants import CONSTANTS

database = join(CONSTANTS['ROOT'], 'db.json')

def dump(data,file):
    json.dump(data,file,indent=2,sort_keys=True)


def initialize():
    # create db.json file in ./server
    if(os.path.exists(database) == False):
        with open(database,"a+") as file:
            db = {}
            db["todos"] = {}
            dump(db,file)
    pass

def create_todo(payload):
    if(os.path.exists(database)):
        with open(database) as file:
            try:
                obj = json.load(file)
                obj["todos"][payload["id"]] = payload
                with open(database, "w") as f:
                    dump(obj,f)
                    # return todo with @id and @date
                return obj["todos"][payload["id"]]
            except Exception as e:
                print("APPENDING TO FILE FAILED todo:{} exception: {}".format(payload["todo"],e))


def delete_todo(id):
    if(os.path.exists(database)):
        with open(database) as file:
            try:
                obj = json.load(file)
                if id in obj["todos"]:
                    del obj["todos"][id]
                with open(database, "w") as f:
                    dump(obj,f)

            except Exception as e:
                print("DELETE id:{} FAILED exception: {}".format(id,e))


def update_todo(payload):
    if(os.path.exists(database)):
        with open(database) as file:
            try:
                obj = json.load(file)
                if payload["id"] in obj["todos"]:
                    with open(database, "w") as f:
                        obj["todos"][payload["id"]] =  {
                            **obj["todos"][payload["id"]],
                            **payload
                        }
                        dump(obj,f)
                        return obj["todos"][payload["id"]] # return the modified todo

            except Exception as e:
                print("PATCH id:{} FAILED exception: {}".format(payload["id"],e))


def todos():
    with open(database,"r") as file:
        try:
            data = json.load(file)
            return data
        except Exception as e:
            print("CREATING TODOS RESPONSE FROM JSON FILE exception: {}".format(e))