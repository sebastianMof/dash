from model import db

class Curso(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  jornada_id = db.Column(db.Integer, db.ForeignKey("jornada.id"), nullable=False)
  grado_id = db.Column(db.Integer, db.ForeignKey("grado.id"), nullable=False)
  letra = db.Column(db.String(1), nullable=False)
  
  def __init__(self, jornada_id, grado_id, letra):
    self.grado_id = grado_id
    self.jornada_id = jornada_id
    self.letra = letra
    

