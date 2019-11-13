from flask import Flask
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
full_list = ['Beater', 'My Winner', "Santa's little runner", 'Big money', 'Ruby Gold']
tracking_list = []
@app.route("/")
def hello():
    return "Welcome to the somber-bets backend! This message is mostly used for testing"

@app.route("/add/<horse>")
def add_in(horse):
    with open('data/tracked-horses.json', 'r') as f:
        horses = json.load(f)
    horses['tracked'].append(horse)
    with open('data/tracked-horses.json', 'w') as f:
        json.dump(horses, f)
    return "Ok " + str(horse) + " will be added"

@app.route("/remove/<horse>")
def remove_now(horse):
    with open('data/tracked-horses.json', 'r') as f:
        horses = json.load(f)
    horses['tracked'].remove(horse)
    with open('data/tracked-horses.json', 'w') as f:
        json.dump(horses, f)
    return "Ok " + str(horse) + " will be removed"

@app.route("/horses")
def horses_call():
    with open('data/tracked-horses.json', 'r') as f:
        return json.load(f)


if __name__ == "__main__":
    app.run(host="127.0.0.1",port=82)