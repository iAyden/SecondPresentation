from db_manager import obtener_personajes_por_equipo, guardar_batalla
class Batalla:
    def __init__(self, equipo1_id, equipo2_id):
        self.equipo1_id = equipo1_id
        self.equipo2_id = equipo2_id
        self.equipo1 = self.cargar_equipo(equipo1_id)
        self.equipo2 = self.cargar_equipo(equipo2_id)

    def cargar_equipo(self, equipo_id):
        miembros = obtener_personajes_por_equipo(equipo_id)
        return [{"Nombre": p[1], "Fuerza": p[3], "Velocidad": p[4], "Inteligencia": p[5]} for p in miembros]

    def calcular_poder_equipo(self, equipo):
        return sum(p["Fuerza"] + p["Velocidad"] + p["Inteligencia"] for p in equipo)

    def simular_batalla(self):
        poder_equipo1 = self.calcular_poder_equipo(self.equipo1)
        poder_equipo2 = self.calcular_poder_equipo(self.equipo2)

        ganador_id = self.equipo1_id if poder_equipo1 > poder_equipo2 else self.equipo2_id
        guardar_batalla(self.equipo1_id, self.equipo2_id, ganador_id)

        return {
            "Equipo1": self.equipo1,
            "Equipo2": self.equipo2,
            "Ganador": ganador_id,
            "PoderEquipo1": poder_equipo1,
            "PoderEquipo2": poder_equipo2
        }
