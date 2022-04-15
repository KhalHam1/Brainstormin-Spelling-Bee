from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin, LoginManager
from App.database import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    highscore_easy = db.Column(db.Integer)
    highscore_medium = db.Column(db.Integer)
    highscore_hard = db.Column(db.Integer)

    def __init__(self, username, password, highscore):
        self.username = username
        self.set_password(password)
        self.highscore_easy = highscore
        self.highscore_medium = highscore
        self.highscore_hard = highscore



    def toDict(self):
        return{
            'id': self.id,
            'username': self.username,
            'highscore_easy': self.highscore_easy,
            'highscore_medium': self.highscore_medium,
            'highscore_hard': self.highscore_hard
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    
    

