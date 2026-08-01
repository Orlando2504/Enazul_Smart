# =====================================
# ENAZUL SMART RC1
# Motor de Evaluación
# =====================================

from motor.reglas import (
    validar_edad,
    validar_ingreso,
    validar_contrato,
    validar_antiguedad,
    validar_entidades,
    validar_perdidas,
    validar_institucion
)


def evaluar(solicitud):

    errores = []
    observaciones = []
    score = 100

    # Edad
    ok, mensaje = validar_edad(solicitud.edad)

    if ok:
        observaciones.append("Edad válida.")
    else:
        errores.append(mensaje)
        score -= 20

    # Ingreso
    ok, mensaje = validar_ingreso(solicitud.ingreso)

    if ok:
        observaciones.append("Ingreso líquido válido.")
    else:
        errores.append(mensaje)
        score -= 25

    # Contrato
    ok, mensaje = validar_contrato(solicitud.contrato)

    if ok:
        observaciones.append("Contrato permitido.")
    else:
        errores.append(mensaje)
        score -= 15

    # Antigüedad
    ok, mensaje = validar_antiguedad(
        solicitud.contrato,
        solicitud.antiguedad
    )

    if ok:
        observaciones.append("Antigüedad suficiente.")
    else:
        errores.append(mensaje)
        score -= 15

    # Entidades
    ok, mensaje = validar_entidades(
        solicitud.entidades
    )

    if ok:
        observaciones.append("Cantidad de entidades aceptable.")
    else:
        errores.append(mensaje)
        score -= 15

    # Pérdidas
    ok, mensaje = validar_perdidas(
        solicitud.perdidas
    )

    if ok:
        observaciones.append("Historial dentro del límite.")
    else:
        errores.append(mensaje)
        score -= 20

    # Institución
    ok, mensaje = validar_institucion(
        solicitud.institucion,
        solicitud.porta_arma
    )

    if ok:
        observaciones.append("Institución permitida.")
    else:
        errores.append(mensaje)
        score -= 25

    # Nunca negativo
    if score < 0:
        score = 0

    # Nivel de riesgo
    if score >= 90:
        riesgo = "BAJO"
    elif score >= 70:
        riesgo = "MEDIO"
    else:
        riesgo = "ALTO"

    # Estado
    if len(errores) == 0:

        estado = "PRECALIFICA"

    else:

        estado = "NO PRECALIFICA"

    return {

        "estado": estado,

        "score": score,

        "riesgo": riesgo,

        "observaciones": observaciones,

        "errores": errores

    }