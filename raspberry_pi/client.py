import requests
import time

import mechanical_ops as mech

import pyrebase
from signal import pause

config = {
  "apiKey": "apiKey",
  "authDomain": "crawler-561c8.firebaseapp.com",
  "databaseURL": "https://crawler-561c8.firebaseio.com",
  "storageBucket": "crawler-561c8.appspot.com",
#   "serviceAccount": "path/to/serviceAccountCredentials.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def state_needed(message):
    db.update({"state_list": mech.get_state(), "state_needed": 1})

def set_action(message):
    action_list = message["data"]
    mech.set_speed(action_list)
    time.sleep(0.3)
try:
    db.child("state_needed").stream(state_needed)
    db.child("action_list").stream(set_action)
    print("Ready")
    pause()
except KeyboardInterrupt:
    print("Exiting...")