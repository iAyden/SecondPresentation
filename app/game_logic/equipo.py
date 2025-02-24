from app.models import Equipo

def crear_equipo(id, nombre):
    return Equipo(id, nombre)