from flask import Blueprint, jsonify, request, render_template
from db_manager import obtener_personajes, obtener_equipos, crear_equipo, agregar_personaje_a_equipo
from app.game_logic.batalla import Batalla

routes = Blueprint("routes", __name__)

@routes.route("/")
def index():
    return render_template("index.html")

@routes.route("/personajes", methods=["GET"])
def personajes():
    return jsonify([{
        "ID": p[0], "Nombre": p[1], "Universo": p[2], 
        "Fuerza": p[3], "Velocidad": p[4], "Inteligencia": p[5], 
        "Habilidad": p[6]
    } for p in obtener_personajes()])

@routes.route("/equipos", methods=["GET"])
def equipos():
    return jsonify([{
        "ID": e[0], "Nombre": e[1]
    } for e in obtener_equipos()])

@routes.route("/equipos", methods=["POST"])
def crear_nuevo_equipo():
    data = request.json
    crear_equipo(data["nombre"])
    return jsonify({"mensaje": "Equipo creado exitosamente"}), 201

@routes.route("/equipos/<int:equipo_id>/agregar_personaje", methods=["POST"])
def agregar_personaje_al_equipo(equipo_id):
    data = request.json
    agregar_personaje_a_equipo(equipo_id, data["personaje_id"])
    return jsonify({"mensaje": "Personaje agregado al equipo exitosamente"}), 200

@routes.route("/batalla", methods=["POST"])
def batalla():
    data = request.json
    batalla = Batalla(data["equipo1_id"], data["equipo2_id"])
    resultado = batalla.simular_batalla()
    return jsonify(resultado)