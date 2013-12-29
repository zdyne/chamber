"""
Copyright 2013, Patrick J. Franz
"""

import wtforms
from wtforms import validators
from flask.ext import wtf


class LoginForm(wtf.Form):
    userName = wtforms.TextField('userName', validators=[validators.Required()])
    userPass = wtforms.PasswordField('userPass')
    rememberMe = wtforms.BooleanField('rememberMe', default=False)
