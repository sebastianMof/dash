from model import db

class Jornada(db.Model):
  id = db.Column(db.Integer, primary_key=True)
