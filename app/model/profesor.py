from model import db

class Profesor(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=True)
  jornada_id = db.Column(db.Integer, db.ForeignKey("jornada.id"), nullable=False)

  def __init__(self, usuario_id, jornada_id):
    self.usuario_id = usuario_id
    self.jornada_id = jornada_id