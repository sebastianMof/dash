from model import db

class BloqueJornada(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  bloque_id = db.Column(db.Integer, db.ForeignKey("bloque.id"), nullable=False)
  jornada_id = db.Column(db.Integer, db.ForeignKey("jornada.id"), nullable=False)
  
  def __init__(self, bloque_id, jornada_id):
    self.bloque_id = bloque_id
    self.jornada_id = jornada_id
