from app import app
from flask import render_template


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home page')


@app.route('/club')
def club():
    return render_template('club.html', title='Club')


@app.route('/join')
def join():
    return render_template('join.html', title='Join Us')


@app.route('/supporter')
def supporter():
    return render_template('supporter.html', title='Supporter')


@app.route('/team')
def team():
    return render_template('team.html', title='Team')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contacts')


@app.route('/project')
def project():
    return render_template('project.html', title='Project')
