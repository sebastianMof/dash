from model import db

class Sugerencia(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  profesor_id = db.Column(db.Integer, db.ForeignKey("profesor.id"), nullable=False)
  titulo = db.Column(db.String(50), nullable=False)
  contenido = db.Column(db.String(500), nullable=False)
  estado = db.Column(db.String(50), nullable=False)
  
  def __init__(self, profesor_id, titulo, contenido, estado):
    self.profesor_id = profesor_id
    self.titulo = titulo
    self.contenido = contenido
    self.estado = estado

