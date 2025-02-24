class Personaje:
    def __init__(self, id, nombre, universo, fuerza, velocidad, inteligencia, habilidad_especial):
        self.id = id
        self.nombre = nombre
        self.universo = universo
        self.fuerza = fuerza
        self.velocidad = velocidad
        self.inteligencia = inteligencia
        self.habilidad_especial = habilidad_especial

    def __str__(self):
        return f"{self.nombre} (Universo: {self.universo}, Fuerza: {self.fuerza}, Velocidad: {self.velocidad}, Inteligencia: {self.inteligencia}, Habilidad: {self.habilidad_especial})"

class Equipo:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.miembros = [] 

    def agregar_personaje(self, personaje):
        self.miembros.append(personaje)

    def eliminar_personaje(self, personaje):
        self.miembros.remove(personaje)

    def __str__(self):
        return f"Equipo: {self.nombre} - Miembros: {[p.nombre for p in self.miembros]}"