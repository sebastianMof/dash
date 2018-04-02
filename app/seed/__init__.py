import datetime
from model import *

def seed(init_db):
  
#-----------BLOQUES-------------#
                    #HoraInicio          HoraTermino          Dia#
  LA = bloque.Bloque(datetime.time(8,0), datetime.time(9,30), 'Lunes')  #1
  MA = bloque.Bloque(datetime.time(8,0), datetime.time(9,30), 'Martes') #2
#-----------USUARIOS------------#
                            #Rut            Nombre            Email                 Password#
  alan =    usuario.Usuario('10.010.010-0', 'Alan Brito',     "alan@brito.com",     "123") #1
  aquiles = usuario.Usuario('11.011.011-1', 'Aquiles Brinco', "aquiles@brinco.com", "123") #2
  elba =    usuario.Usuario('12.012.012-2', 'Elba Lazo',    "elba@zurita.com",    "123") #3
#-----------JORNADAS------------#
  jornada_alan =    jornada.Jornada() #1
  jornada_aquiles = jornada.Jornada() #2
  jornada_septimo = jornada.Jornada() #3
  jornada_octavo =  jornada.Jornada() #4
#----------PROFESORES-----------#
                                      #Usuario Jornada#
  profesor_alan =    profesor.Profesor(1,      1) #1
  profesor_aquiles = profesor.Profesor(2,      2) #2
#------------GRADOS-------------#
                       #Nombre#
  septimo = grado.Grado('Septimo') #1
  octavo =  grado.Grado('Octavo')  #2
#---------ASIGNATURA------------#
                                  #Nombre#
  lenguaje = asignatura.Asignatura('Lenguaje') #1 
#-------GRADO-ASIGNATURA--------#
                                                     #Grado Asignatura#
  septimo_lenguaje = grado_asignatura.GradoAsignatura(1,    1) #1
  octavo_lenguaje =  grado_asignatura.GradoAsignatura(2,    1) #2
#-----ASIGNATURA-PROFESOR-------#
                                                                  #GradoAsignatura Profesor#
  lenguaje_septimo_alan =   asignatura_profesor.AsignaturaProfesor(1,              1) #1
  lenguaje_octavo_aquiles = asignatura_profesor.AsignaturaProfesor(2,              2) #3
#------------CURSOS-------------#
                         #Jornada Grado Letra#
  septimo_a = curso.Curso(3,      1,    'a') #1
  octavo_a =  curso.Curso(4,      2,    'a') #2
#---------BLOQUE-JORNADA--------# 
                                             #Bloque Jornada#
  LA_alan =      bloque_jornada.BloqueJornada(1,     1) #1
  MA_alan =      bloque_jornada.BloqueJornada(2,     1) #2
  LA_aquiles =   bloque_jornada.BloqueJornada(1,     2) #3
  LA_septimo_a = bloque_jornada.BloqueJornada(1,     3) #4
  MA_septimo_a = bloque_jornada.BloqueJornada(2,     3) #5
  LA_octavo_a =  bloque_jornada.BloqueJornada(1,     4) #6
  MA_octavo_a =  bloque_jornada.BloqueJornada(2,     4) #7
#--------HORARIO-ESCOLAR--------#
                                                    #Publicado#
  horario_publicado = horario_escolar.HorarioEscolar(True) #1
#-----------HORARIOS------------#
                                     #HorarioEscolar#
  horario_septimo_a = horario.Horario(1) #1
  horario_octavo_a =  horario.Horario(1) #2
#---------BLOQUE-HORARIO--------#
                                      #Horario Bloque Curso Asignatura Profesor#
  LA_septimo_alan =    bloque_horario.BloqueHorario(1,      1,     1,    1,         1) #1
  LA_octavo_aquiles =  bloque_horario.BloqueHorario(2,      1,     2,    1,         2) #2

#----------SUGERENCIAS----------#
                                           #Profesor Titulo                    Contenido  Estado#
  sugerencia_alan_1 = sugerencia.Sugerencia(1,       'Cambio de dia',          'Martes',  'Aceptado')  #1
  sugerencia_alan_2 = sugerencia.Sugerencia(1,       'No quiero trabajar',     ':('    ,  'Rechazado') #2
  sugerencia_alan_3 = sugerencia.Sugerencia(1,       'Cambio de dia otra vez', 'Viernes', 'Espera')    #3
#-----------RESPUESTA-----------# 
  respuesta_sugerencia_2 = respuesta.Respuesta(2, 'shiaa')
#---------ADMINISTRADOR---------#   
                                                  #Usuario#
  administrador_elba = administrador.Administrador(3) #1

  init_db.session.add(LA)
  init_db.session.add(MA)
  init_db.session.add(alan)
  init_db.session.add(aquiles)
  init_db.session.add(elba)
  init_db.session.add(jornada_alan)
  init_db.session.add(jornada_aquiles)
  init_db.session.add(jornada_octavo)
  init_db.session.add(jornada_septimo)
  init_db.session.add(profesor_alan)
  init_db.session.add(profesor_aquiles)
  init_db.session.add(septimo)
  init_db.session.add(octavo)
  init_db.session.add(lenguaje)
  init_db.session.add(septimo_lenguaje)
  init_db.session.add(octavo_lenguaje)
  init_db.session.add(lenguaje_septimo_alan)
  init_db.session.add(lenguaje_octavo_aquiles)
  init_db.session.add(septimo_a)
  init_db.session.add(octavo_a)
  init_db.session.add(LA_alan)
  init_db.session.add(LA_aquiles)
  init_db.session.add(LA_septimo_a)
  init_db.session.add(LA_octavo_a)
  init_db.session.add(MA_alan)
  init_db.session.add(MA_septimo_a)
  init_db.session.add(MA_octavo_a)
  init_db.session.add(horario_publicado)
  init_db.session.add(horario_septimo_a)
  init_db.session.add(horario_octavo_a)
  init_db.session.add(LA_septimo_alan)
  init_db.session.add(LA_octavo_aquiles)
  init_db.session.add(sugerencia_alan_1)
  init_db.session.add(sugerencia_alan_2)
  init_db.session.add(sugerencia_alan_3)
  init_db.session.add(respuesta_sugerencia_2)
  init_db.session.add(administrador_elba)

  init_db.session.commit()