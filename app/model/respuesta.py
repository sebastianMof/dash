from model import db

class Respuesta(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  sugerencia_id = db.Column(db.Integer, db.ForeignKey("sugerencia.id"), nullable=False)
  contenido = db.Column(db.String(500), nullable=False)
  
  def __init__(self, sugerencia_id, contenido):
    self.sugerencia_id = sugerencia_id
    self.contenido = contenido
