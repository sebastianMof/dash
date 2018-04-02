from model import db

class Grado(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(50), unique=True, nullable=False)
  
  def __init__(self, nombre):
    self.nombre = nombre

