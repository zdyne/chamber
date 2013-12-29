"""
Copyright 2013, Patrick J. Franz
"""

import flask
from flask.ext import login

import forms
from app import app
from app import loginManager
from app import models
from app import bcrypt


@app.before_request
def before_request():
    flask.g.user = login.current_user

@loginManager.user_loader
def loadUser(uid):
    return models.User.query.get(int(uid))

# View endpoints

@app.route('/')
@app.route('/index')
@login.login_required
def indexRoute():
    return flask.render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def loginRoute():
    if flask.g.user is not None and flask.g.user.is_authenticated():
        return flask.redirect(flask.url_for('indexRoute'))

    form = forms.LoginForm()

    if form.validate_on_submit():
        user = models.User.query.filter_by(email=form.userName.data).first()

        if user and bcrypt.check_password_hash(user.password, form.userPass.data):
            flask.session['rememberMe'] = form.rememberMe.data
            login.login_user(user, flask.session['rememberMe'])

            return flask.redirect(flask.url_for('indexRoute'))            

    return flask.render_template('login.html', form=form)

@app.route('/logout')
@login.login_required
def logoutRoute():
    login.logout_user()
    return flask.redirect(flask.url_for('loginRoute'))

# REST endpoints
