from app import db,login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index = True, unique = True)
    classname = db.Column(db.String(64), index=True, unique=False)
    role = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    
    def __repr__(self):
        return '<User {}>'.format(self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class SpellingTest(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    duedate = db.Column(db.DateTime)

class TestWords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey(SpellingTest.id) )
    word = db.Column(db.String(128), index = True)
    samplesentence = db.Column(db.String(512))

    def __repr__(self):
        return '<Word {}>'.format(self.word)
        

class TestResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey(User.id))
    spellingtest_id = db.Column(db.Integer,db.ForeignKey(SpellingTest.id))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow )
    score = db.Column(db.Integer, index=True)

    

