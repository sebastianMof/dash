from model import db

class HorarioEscolar(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  publicado = db.Column(db.Boolean)
  
  def __init__(self, publicado):
    self.publicado = publicado
