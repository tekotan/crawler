from flask import Flask, request, jsonify

app = Flask(__name__)

states = {
    "state_needed": True,
    "action_needed": False,
    "state_list": [1],
    "action_list": [1],
}

@app.route('/state_needed')
def state_needed():
    return states["state_needed"]

@app.route('/action_needed')
def action_needed():
    return states["action_needed"]

@app.route('/post_state', methods=["POST"]) 
def post_state():
    state_list = list(map(int, request.data.split(", ")))
    states["state_list"] = state_list

@app.route('/post_action', methods=["POST"]) 
def post_action():
    # print(request.data)
    action_list = list(map(int, request.data.decode().split(", ")))
    states["action_list"] = action_list
    return ""

@app.route("/get_action")
def get_action():
    return str(states["action_list"]).strip("[]")

@app.route("/get_state")
def get_state():
    return str(states["state_list"]).strip("[]")

app.run(host="localhost", port=6006, debug=True)