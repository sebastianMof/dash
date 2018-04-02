from model import db

class Asignatura(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(50), nullable=False, unique=True)
  
  def __init__(self, nombre):
    self.nombre = nombre