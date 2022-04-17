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


def update_user_score(username, difficulty, score):
    user_to_update = User.query.filter_by(username=username).first()
    if difficulty == 'easy':
        if score > user_to_update.highscore_easy:
            user_to_update.highscore_easy = score
            db.session.add(user_to_update)
    
    if difficulty == 'medium':
        if score > user_to_update.highscore_medium:
            user_to_update.highscore_medium = score
            db.session.add(user_to_update)
    
    if difficulty == 'hard':
        if score > user_to_update.highscore_hard:
            user_to_update.highscore_hard = score
            db.session.add(user_to_update)  

    if difficulty == 'genius':
        if score > user_to_update.highscore_genius:
            user_to_update.highscore_genius = score
            db.session.add(user_to_update)    
    
    db.session.commit()

def get_elementary_scores():  
    # elementary = {
    #         username: '',
    #         elementary_score: 0
    #     }   
    scores = []
    all_users = get_all_users()
    for user in all_users:
        userDict = user.toDict()
        curr_score = userDict['highscore_easy']
        curr_user = userDict['username']
        if curr_score != 0:
            elementary = {
            "username": curr_user,
            "elementary_score":curr_score
            }   
            scores.append(elementary)
        

    min = 10000000000
    min_pos = 0
    length = len(scores)
    for m in range(0,length):
        current = scores[m]
        curr_val = current['elementary_score']
        if curr_val<min:
            min_pos = m

    for i in range(length):
        lowest_index = min_pos
        curr = scores[lowest_index]
        curr_score2 = curr['elementary_score']
        for j in range(i+1,length):
            prev = scores[j]
            prev_score = prev['elementary_score']
            if prev_score < curr_score2:
                lowest_index = j
    
        scores[i], scores[lowest_index] = scores[lowest_index], scores[i]

    scores.reverse()

    return scores


def get_secondary_scores():  
    
    scores = []
    all_users = get_all_users()
    for user in all_users:
        userDict = user.toDict()
        curr_score = userDict['highscore_medium']
        curr_user = userDict['username']
        if curr_score != 0:
            secondary = {
            "username": curr_user,
            "secondary_score":curr_score
            }   
            scores.append(secondary)
        

    min = 10000000000
    min_pos = 0
    length = len(scores)
    for m in range(0,length):
        current = scores[m]
        curr_val = current['secondary_score']
        if curr_val<min:
            min_pos = m

    for i in range(length):
        lowest_index = min_pos
        curr = scores[lowest_index]
        curr_score2 = curr['secondary_score']
        for j in range(i+1,length):
            prev = scores[j]
            prev_score = prev['secondary_score']
            if prev_score < curr_score2:
                lowest_index = j
    
        scores[i], scores[lowest_index] = scores[lowest_index], scores[i]

    scores.reverse()

    return scores

def get_university_scores():  
    
    scores = []
    all_users = get_all_users()
    for user in all_users:
        userDict = user.toDict()
        curr_score = userDict['highscore_hard']
        curr_user = userDict['username']
        if curr_score != 0:
            university = {
            "username": curr_user,
            "university_score":curr_score
            }   
            scores.append(university)

    min = 10000000000
    min_pos = 0
    length = len(scores)
    for m in range(0,length):
        current = scores[m]
        curr_val = current['university_score']
        if curr_val<=min:
            min_pos = m

    for i in range(length):
        lowest_index = min_pos
        curr = scores[lowest_index]
        curr_score2 = curr['university_score']
        for j in range(i+1,length):
            prev = scores[j]
            prev_score = prev['university_score']
            if prev_score < curr_score2:
                lowest_index = j
    
        scores[i], scores[lowest_index] = scores[lowest_index], scores[i]

    scores.reverse()

    return scores

def get_genius_scores():  
    scores = []
    all_users = get_all_users()
    for user in all_users:
        userDict = user.toDict()
        curr_score = userDict['highscore_genius']
        curr_user = userDict['username']
        if curr_score != 0:
            genius = {
            "username": curr_user,
            "genius_score":curr_score
            }   
            scores.append(genius)

    min = 10000000000
    min_pos = 0
    length = len(scores)
    for m in range(0,length):
        current = scores[m]
        curr_val = current['genius_score']
        if curr_val<=min:
            min_pos = m

    for i in range(length):
        lowest_index = min_pos
        curr = scores[lowest_index]
        curr_score2 = curr['genius_score']
        for j in range(i+1,length):
            prev = scores[j]
            prev_score = prev['genius_score']
            if prev_score < curr_score2:
                lowest_index = j
    
        scores[i], scores[lowest_index] = scores[lowest_index], scores[i]

    scores.reverse()

    return scores
    







    