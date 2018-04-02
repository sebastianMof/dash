from model import db

class Horario(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  horario_escolar_id = db.Column(db.Integer, db.ForeignKey("horario_escolar.id"), nullable=False)
  
  def __init__(self, horario_escolar_id):
    self.horario_escolar_id = horario_escolar_id
