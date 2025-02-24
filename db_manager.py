import pyodbc
from config import DB_CONFIG

def conectar_db():
    return pyodbc.connect(
        f"DRIVER={DB_CONFIG['DRIVER']};"
        f"SERVER={DB_CONFIG['SERVER']};"
        f"DATABASE={DB_CONFIG['DATABASE']};"
        f"UID={DB_CONFIG['UID']};"
        f"PWD={DB_CONFIG['PWD']};"
    )
def obtener_personajes():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Personajes")
    personajes = cursor.fetchall()
    conn.close()
    return personajes

def obtener_equipos():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Equipos")
    equipos = cursor.fetchall()
    conn.close()
    return equipos

def crear_equipo(nombre):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Equipos (Nombre) VALUES (?)", nombre)
    conn.commit()
    conn.close()

def agregar_personaje_a_equipo(equipo_id, personaje_id):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Equipo_Personaje (EquipoID, PersonajeID) VALUES (?, ?)", equipo_id, personaje_id)
    conn.commit()
    conn.close()

def guardar_batalla(equipo1_id, equipo2_id, ganador_id):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Batallas (Equipo1ID, Equipo2ID, GanadorID) VALUES (?, ?, ?)", equipo1_id, equipo2_id, ganador_id)
    conn.commit()
    conn.close()
def obtener_personajes_por_equipo(equipo_id):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.* 
        FROM Personajes p
        JOIN Equipo_Personaje ep ON p.ID = ep.PersonajeID
        WHERE ep.EquipoID = ?
    """, equipo_id)
    personajes = cursor.fetchall()
    conn.close()
    return personajes