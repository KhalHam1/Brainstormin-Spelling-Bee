from flask import Blueprint, redirect, render_template, request, send_from_directory, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo, Email

api_views = Blueprint('api_views', __name__, template_folder='../templates')

class login_button(FlaskForm):
  submit = SubmitField('Login', render_kw={'class': 'btn waves-effect waves-light white-text'})

class signup_button(FlaskForm):
  submit = SubmitField('Sign Up', render_kw={'class': 'btn waves-effect waves-light white-text'})

# @api_views.route('/', methods=['GET'])
# def get_api_docs():
#     form = signup_button()
#     return render_template('index.html',form=form)
    