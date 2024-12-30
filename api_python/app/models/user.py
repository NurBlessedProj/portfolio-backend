from app import db

class User(db.Model):
    id = db.Column(db.integer, primary_key=True)
    username = db.Column(db.strng(50), unique=True, nullable=False)
    email = db.Column(db.string(100), unique=True, nullable=True)
    
    def __repr__(self):
      return f"<User {self.username}>"
