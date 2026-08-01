from flask import Blueprint, render_template, request, jsonify

from motor.modelos import Solicitud
from motor.evaluacion import evaluar
from services.database import guardar_solicitud

formulario_bp = Blueprint("formulario", __name__)


@formulario_bp.route("/formulario")
def formulario():

    return render_template("formulario.html")


@formulario_bp.route("/resultado")
def resultado():

    return render_template("resultado.html")


@formulario_bp.route("/evaluar", methods=["POST"])
def evaluar_solicitud():

    datos = request.get_json()

    solicitud = Solicitud(
        edad=int(datos["edad"]),
        ingreso=float(datos["ingreso"]),
        contrato=datos["contrato"],
        institucion=datos["institucion"],
        antiguedad=int(datos["antiguedad"]),
        entidades=int(datos["entidades"]),
        perdidas=int(datos["perdidas"]),
        porta_arma=datos["porta_arma"]
    )

    resultado = evaluar(solicitud)

    registro = {

        "nombre": datos["nombre"],
        "documento": datos["documento"],
        "celular": datos["celular"],
        "correo": datos["correo"],

        "institucion": datos["institucion"],
        "contrato": datos["contrato"],
        "antiguedad": datos["antiguedad"],
        "ingreso": datos["ingreso"],
        "edad": datos["edad"],
        "entidades": datos["entidades"],
        "perdidas": datos["perdidas"],
        "porta_arma": datos["porta_arma"],

        "estado": resultado["estado"],
        "score": resultado["score"],
        "riesgo": resultado["riesgo"]

    }

    guardar_solicitud(registro)

    return jsonify(resultado)