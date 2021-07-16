from application import db

class Story(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    character = db.Column(db.String(30))
    background = db.Column(db.String(100))
    endpoint = db.Column(db.String(300))