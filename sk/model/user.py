from app import db 

class users(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(100))