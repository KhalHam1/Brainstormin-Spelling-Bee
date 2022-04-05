from App.models import User
from App.database import db
from flask_login import UserMixin, LoginManager, login_user, current_user
# from App.main import login_manager



login_manager = LoginManager()
# ''' Begin Flask Login Functions '''
#login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# ''' End Flask Login Functions '''

def get_loggedin_user():
    # return current_user.username
    # if current_user.
    # return login_manager
    pass

def get_all_users():
    return User.query.all()

def create_user(username, password, highscore):
    newuser = User(username=username, password=password, highscore=highscore)
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
    if user:
        userDict = user.toDict()
        return int(userDict['id'])
    return None
    

def get_user_object(username):
    user = User.query.filter_by(username=username).first()
    return user

def delete_user(id):
    user_to_delete = User.query.get(id)
    db.session.delete(user_to_delete)
    db.session.commit()




    