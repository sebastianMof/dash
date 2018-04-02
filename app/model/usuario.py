import uuid
import hashlib
from model import db

def hash_password(password):
  salt = uuid.uuid4().hex
  return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, user_password):
  password, salt = hashed_password.split(':')
  return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

class Usuario(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  rut =  db.Column(db.String(120), unique=True, nullable=False)
  nombre = db.Column(db.String(80), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(120), nullable=False)

  def __init__(self, rut, nombre, email, password):
    self.rut = rut
    self.nombre = nombre
    self.email = email
    self.password = hash_password(password)

  def __repr__(self):
    return '<User %r>' % self.username