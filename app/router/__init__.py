from flask import Blueprint, render_template, abort, redirect, url_for, request, Response, session
from jinja2 import TemplateNotFound
from model import usuario
from model.profesor import Profesor
from model.administrador import Administrador
from model.sugerencia import Sugerencia
from model.respuesta import Respuesta
from model.horario_escolar import HorarioEscolar
from model.horario import Horario
from model.bloque import Bloque
from model.bloque_horario import BloqueHorario
from model.asignatura import Asignatura
from model.curso import Curso

routes = Blueprint('routes', __name__, template_folder='templates')

def verificar_usuario(username, password):
  usuario_login = usuario.Usuario.query.filter_by(rut=username).first()
  if usuario_login is None:
    return False
  if usuario.check_password(usuario_login.password, password):
    profesor_check = Profesor.query.filter_by(usuario_id=usuario_login.id).first()
    administrador_check = Administrador.query.filter_by(usuario_id=usuario_login.id).first()
    if profesor_check is not None:
      session['usuario'] = 'profesor'
      session['profesor_id'] = profesor_check.id
      return True
    elif administrador_check is not None:
      session['usuario'] = 'administrador'
      return True
  return False


@routes.route('/login', methods=['POST', 'GET'])
def login():
  if request.method == 'POST':
    if not verificar_usuario(request.form['nombre'], request.form['password']):
      return redirect(url_for('routes.login'))
    if session.get('usuario') is 'profesor':
      return redirect(url_for('routes.profesor'))
    elif session.get('usuario') is 'administrador':
      return redirect(url_for('routes.horarios'))
  else:
    return render_template('login.html')

@routes.route('/logout')
def logout():
  session['usuario'] = None
  session['profesor_id'] = None
  return redirect(url_for('routes.login'))

@routes.route('/sugerencias')
def sugerencias():
  try:
    if session['usuario'] != 'profesor':
  	  return redirect(url_for('routes.logout'))
    sugerencias = []
    q = Sugerencia.query.filter_by(profesor_id=1).all()
    for sugerencia in q:
      r = Respuesta.query.filter_by(sugerencia_id=sugerencia.id)
      sugerencias.append({'sugerencia':sugerencia,'respuestas':r})

    return render_template('sugerencias-profesor.html', sugerencias = sugerencias)
  except TemplateNotFound:
    abort(404)

@routes.route('/administrador/horarios')
def horarios():
  try:
    if session.get('usuario') != 'administrador':
      return redirect(url_for('routes.logout'))
    x = []
    hc = HorarioEscolar.query.all()
    i = 0
    j = 0
    for sets in hc:
      x.append({'set':hc, 'horarios':[]})
      h = Horario.query.filter_by(horario_escolar_id=sets.id).all()
      for horarios in h:
        x[i]['horarios'].append({'horario':h, 'bloques':[]})
        b = BloqueHorario.query.filter_by(horario_id=horarios.id).all()
        for bloques in b:
          p = Profesor.query.filter_by(id=bloques.profesor_id).all()
          a = Asignatura.query.filter_by(id=bloques.asignatura_id).all()
          c = Curso.query.filter_by(id=bloques.curso_id).all()
          r = Bloque.query.filter_by(id=bloques.bloque_id).all()
          x[i]['horarios'][j]['bloques'].append({'bloque_horario':b, 'profesor':p, 'asignatura':a, 'curso':c, 'bloque':r})
        j +=1
      i += 1

    return render_template('horarios-administrador.html', horarios = x)
  except TemplateNotFound:
    abort(404)

@routes.route('/administrador/<page>')
def administrador(page):
  try:
    if session.get('usuario') != 'administrador':
  	  return redirect(url_for('routes.logout'))
    return render_template('%s-administrador.html' % page)
  except TemplateNotFound:
    abort(404)

@routes.route('/', defaults={'page': 'horario'})
@routes.route('/<page>')
def profesor(page):
  try:
    if session.get('usuario') != 'profesor':
  	  return redirect(url_for('routes.logout'))
    return render_template('%s-profesor.html' % page)
  except TemplateNotFound:
    abort(404)
