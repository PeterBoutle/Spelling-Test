from app import db
from datetime import datetime

class User(db.Model):
    user_id =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index = True, unique = True)
    classname = db.Column(db.String(64), index=True, unique=False)
    role = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

class SpellingTest(db.Model):
    spellingtest_id = db.Column(db.Integer,primary_key=True)
    duedate = db.Column(db.DateTime)

class TestWords(db.Model):
    word_id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey(SpellingTest.spellingtest_id) )
    word = db.Column(db.String(128), index = True)
    samplesentence = db.Column(db.String(512))

    def __repr__(self):
        return '<Word {}>'.format(self.word)
        

class TestResult(db.Model):
    testresult_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey(User.user_id))
    spellingtest_id = db.Column(db.Integer,db.ForeignKey(SpellingTest.spellingtest_id))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow )
    score = db.Column(db.Integer, index=True)

    

