from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
__all__ = ["db", 
           "administrador", 
           "asignatura",
           "asignatura_profesor",
           "bloque",
           "bloque_horario",
           "bloque_jornada",
           "curso",
           "grado",
           "grado_asignatura",
           "horario",
           "horario_escolar",
           "jornada",
           "profesor",
           "respuesta",
           "sugerencia",
           "usuario"]