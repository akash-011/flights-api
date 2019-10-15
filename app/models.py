from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy(db)

class User(db.Model):
    id = db.Column(db.integer, primary_key=True)
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String())

    def __init__(self, email, password):
        self.email = email
        self.password = Bcrypt().generate_password_hash(password).decode()
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    

    
