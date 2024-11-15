from .app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'User(username={self.username}, password={self.password}, age={self.age})'
    
    def get_id(self):
        return self.uid
    

class Post(db.Model):
    __tablename__ = 'posts'
    
    pid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.uid'), nullable=False)
    owner = db.relationship('User', backref='posts')
    
    def __repr__(self) -> str:
        return f'Post(title={self.title}, content={self.content}, owner_id={self.owner_id})'
    
    def get_id(self):
        return self.pid