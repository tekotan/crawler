import requests
import time

import mechanical_ops as mech
address = "http://localhost:6006/"
try:
    while True:
        if requests.get(address + "state_needed"):
            requests.post(url=address + "post_state", data=str(mech.get_state()).strip("[]"))
        if requests.get(address + "action_needed"):
            action_list = list(map(int, requests.get(address + "get_action").split(", ")))
            mech.set_speed(action_list)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Exiting...")