from app.app import db

class User(db.Model):
    __tablename__ = 'users'
    
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'User(username={self.username}, password={self.password}, age={self.age})'
    
    def get_id(self):
        return self.uid