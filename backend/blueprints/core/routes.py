from flask import render_template
from blueprints.core.bp import bp

@bp.route('/')
def home():
    return render_template('hello.html')