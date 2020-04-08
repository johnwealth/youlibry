"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from youlibry import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='YouLibry eLearning Facility | Library Of Libraries',
        year=datetime.now().year,
    )

@app.route('/upload')
def upload():
    """Renders the contact page."""
    return render_template(
        'upload.html',
        title='upload',
        year=datetime.now().year
    )

@app.route('/account')
def account():
    """Renders the contact page."""
    return render_template(
        'account.html',
        title='account',
        year=datetime.now().year
    )

@app.route('/subscriptions')
def subscriptions():
    """Renders the contact page."""
    return render_template(
        'subscriptions.html',
        title='subscriptions',
        year=datetime.now().year
    )

@app.route('/settings')
def settings():
    """Renders the contact page."""
    return render_template(
        'settings.html',
        title='settings',
        year=datetime.now().year
    )

@app.route('/trending')
def trending():
    """Renders the contact page."""
    return render_template(
        'trending.html',
        title='trending',
        year=datetime.now().year
    )

@app.route('/videopage')
def videopage():
    """Renders the contact page."""
    return render_template(
        'video-page.html',
        title='video page',
        year=datetime.now().year
    )

@app.route('/uploadvideo')
def uploadvideo():
    """Renders the contact page."""
    return render_template(
        'upload-video.html',
        title='upload video',
        year=datetime.now().year
    )

@app.route('/libraries')
def libraries():
    """Renders the contact page."""
    return render_template(
        'libraries.html',
        title='libraries',
        year=datetime.now().year
    )

@app.route('/library')
def library():
    """Renders the contact page."""
    return render_template(
        'library.html',
        title='libraries',
        year=datetime.now().year
    )

@app.route('/categories')
def categories():
    """Renders the contact page."""
    return render_template(
        'categories.html',
        title='categories',
        year=datetime.now().year
    )

@app.route('/live')
def live():
    """Renders the contact page."""
    return render_template(
        'live.html',
        title='live',
        year=datetime.now().year
    )

@app.route('/historypage')
def historypage():
    """Renders the contact page."""
    return render_template(
        'historypage.html',
        title='history page',
        year=datetime.now().year
    )

@app.route('/library_account')
def library_account():
    """Renders the contact page."""
    return render_template(
        'library-account.html',
        title='library account',
        year=datetime.now().year
    )

@app.route('/course_category')
def course_category():
    """Renders the contact page."""
    return render_template(
        'course-category.html',
        title='library account',
        year=datetime.now().year
    )

@app.route('/courses')
def courses():
    """Renders the contact page."""
    return render_template(
        'courses.html',
        title='library account',
        year=datetime.now().year
    )

@app.route('/login')
def login():
    """Renders the contact page."""
    return render_template(
        'login.html',
        title='library account',
        year=datetime.now().year
    )