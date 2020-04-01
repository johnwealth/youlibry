from flask import Flask
from blueprints.core import bp as bp_core


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'My_Top_Secert_Key'

    # Blueprint

    bp_core.config(app)

    return app