from app.models import Personaje

def crear_personaje(id, nombre, universo, fuerza, velocidad, inteligencia, habilidad_especial):
    return Personaje(id, nombre, universo, fuerza, velocidad, inteligencia, habilidad_especial)