from flask import Flask
from blueprints.core import bp as bp_core
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

    # Blueprint

    bp_core.config(app)

    return app