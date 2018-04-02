from model import db

class GradoAsignatura(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  grado_id = db.Column(db.Integer, db.ForeignKey("grado.id"), nullable=False)
  asignatura_id = db.Column(db.Integer, db.ForeignKey("asignatura.id"), nullable=False)
  
  def __init__(self, grado_id, asignatura_id):
    self.grado_id = grado_id
    self.asignatura_id = asignatura_id

