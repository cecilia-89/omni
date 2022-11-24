#!/usr/bin/python3
"""Module: flask_app, initializes the flask app"""

from flask import Flask
from flask_cors import CORS
from api.v1.views import app_views

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)

if __name__ == "__main__":
	app.run()
