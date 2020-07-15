import requests
import time

import pyrebase

config = {
  "apiKey": "apiKey",
  "authDomain": "crawler-561c8.firebaseapp.com",
  "databaseURL": "https://crawler-561c8.firebaseio.com",
  "storageBucket": "crawler-561c8.appspot.com",
#   "serviceAccount": "path/to/serviceAccountCredentials.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def set_speed(action_list):
    state_gotten = {"gotten": False}
    def done(message):
        state_gotten["gotten"] = True
    db.update({"action_list": action_list})
    db.update({"action_performed": 0})
    stream = db.child("action_performed").stream(done)
    while not state_gotten["gotten"]:
        pass
    stream.close()
    db.update({"action_performed": 0})

def get_state():
    state_gotten = {"gotten": False, "state_list": []}
    def parse_and_return_state(message):
        state_gotten["state_list"] = db.child("state_list").get().val()
        state_gotten["gotten"] = True
    
    db.update({"state_needed": 1})
    stream = db.child("state_list").stream(parse_and_return_state)
    while not state_gotten["gotten"]:
        pass
    stream.close()
    return state_gotten["state_list"]

def get_action():
    action_list = db.child("action_list").get().val()
    return action_list