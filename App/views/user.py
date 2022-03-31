from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, url_for, redirect
from flask_jwt import jwt_required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo, Email


from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
    check_user,
    get_user,
    get_user_object,
    delete_user
)

class SignUp(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('New Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords Must Match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Sign Up', render_kw={'class': 'btn waves-effect waves-light white-text'})

class LogIn(FlaskForm):
  username = StringField('username', validators=[InputRequired()])
  password = PasswordField('Password', validators=[InputRequired()])
  submit = SubmitField('Login', render_kw={'class': 'btn waves-effect waves-light white-text'})

class login_button(FlaskForm):
  submit = SubmitField('Login', render_kw={'class': 'btn waves-effect waves-light white-text'})

class signup_button(FlaskForm):
  submit = SubmitField('Sign Up', render_kw={'class': 'btn waves-effect waves-light white-text'})

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/', methods=['GET'])
def display_home():
    form=signup_button()
    return render_template('index.html', form=form)

# @user_views.route('/', methods=['POST'])
# def display_home_action1():
#     form = signup_button()
#     return render_template('signup.html',form=form)

@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)


@user_views.route('/api/users')
def client_app():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/signup', methods=['GET'])
def signup():
    form = SignUp()
    return render_template('signup.html', form=form)

@user_views.route('/signup', methods=['POST'])
def signUpAction():
    form = SignUp()
    if form.validate_on_submit():
        data = request.form
        old_user = get_user(username = data['username'])
        if old_user:
            flash('User Already Exists.')
            return render_template('signup.html', form=form)
   
        new_user = create_user(username = data['username'], password=data['password'])
        # new_user.set_password(data['password'])
        flash('Account Created!')
        user = get_user(data['username'])
        print(user)
        return render_template('login.html', form=form)
        # return redirect(url_for('user_views.login'))
    flash('Account Creation Failed!')
    return render_template('signup.html', form=form)
    # return redirect(url_for('signup'))

@user_views.route('/login')
def login():
    form = LogIn()
    return render_template('login.html', form=form)

@user_views.route('/login', methods=['POST'])
def loginAction():
    form = LogIn()
    if form.validate_on_submit():
        data = request.form
        success = check_user(data['username'],data['password'])
        if success:
            flash('Logged In Successfully.')
            user = get_user(data['username'])
            # userId = user
            print(user)
            user_object = get_user_object(data['username'])
            #login_user(user_object)
            return render_template('difficulty.html', form=form)
        flash('Invalid Credentials')
        return render_template('login.html', form=form)


@user_views.route('/delete/<int:id>')  
def delete(id):
    form=signup_button()
    try:
        delete_user(id) 
        flash('User deleted successfully')
        return render_template('index.html', form = form)
    except:
        flash('User was not deleted.')
        return render_template('index.html', form = form)
         

# @app.route('/login', methods=['POST'])
# def loginAction():
#   form = LogIn()
#   if form.validate_on_submit():
#     data = request.form
#     user = User.query.filter_by(username = data['username']).first()
#     if user and user.check_password(data['password']):
#       flash('Logged in successfully.')
#       login_user(user)
#       return redirect(url_for('todos'))
#   flash('Invalid Credentials')
#   return redirect(url_for('index'))

@user_views.route('/api/lol')
def lol():
    return 'lol'

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')