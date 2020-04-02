from flask import render_template
from blueprints.core.bp import bp


@bp.route('/')
@bp.route('/<name>')
def home(name = None):
    return render_template('hello.html', name=name)