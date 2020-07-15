import requests
import time

import pyrebase
import threading

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
    global stream
    result_available = threading.Event()

    def wait():
        def done(message):
            result_available.set()
        db.update({"action_list": action_list})
        db.update({"action_performed": 0})
        global stream
        stream = db.child("action_performed").stream(done)

    thread = threading.Thread(target=wait)
    thread.start()
    result_available.wait()
    stream.close()
    db.update({"action_performed": 0})

def get_state():
    global state_list
    result_available = threading.Event()
    global stream
    def get():
        def parse_and_return_state(message):
            global state_list
            state_list = db.child("state_list").get().val()
            result_available.set()
        
        db.update({"state_needed": 1})
        global stream
        stream = db.child("state_list").stream(parse_and_return_state)

    thread = threading.Thread(target=get)
    thread.start()
    result_available.wait()
    stream.close()
    return state_list

def get_action():
    action_list = db.child("action_list").get().val()
    return action_list