from App.models import User
from App.database import db
from flask_login import UserMixin, LoginManager


def get_all_users():
    return User.query.all()

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toDict() for user in users]
    return users

def get_all_users():
    return User.query.all()

def check_user(username, password):
    user = User.query.filter_by(username = username).first()
    if user and user.check_password(password):
        return True
    return False

def get_user(username):
    user = User.query.filter_by(username=username).first()
    userDict = user.toDict()
    return int(userDict['id'])

def get_user_object(username):
    user = User.query.filter_by(username=username).first()
    return user


    