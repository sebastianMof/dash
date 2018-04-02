from model import db

class AsignaturaProfesor(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  grado_asignatura_id = db.Column(db.Integer, db.ForeignKey("grado_asignatura.id"), nullable=False)
  profesor_id = db.Column(db.Integer, db.ForeignKey("profesor.id"), nullable=False)
  
  def __init__(self, grado_asignatura_id, profesor_id):
    self.grado_asignatura_id = grado_asignatura_id
    self.profesor_id = profesor_id