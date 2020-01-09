from flask import Flask, jsonify
from flask_swagger import swagger

app = Flask(__name__)


@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "My API"
    return jsonify(swag)

@app.route('/')
def index():
    return 'Index Page'

