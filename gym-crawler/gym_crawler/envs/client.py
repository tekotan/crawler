import requests
address = "http://localhost:6006/"

def set_speed(action_list):
    requests.post(url=address + "post_action", data=str(action_list).strip("[]"))

def get_state():
    state_list = list(map(int, requests.get(address + "get_state").text.split(', ')))
    return state_list

def get_action():
    action_list = list(map(int, requests.get(address + "get_action").text.split(", ")))
    return action_list
