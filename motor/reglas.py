# =====================================
# ENAZUL SMART RC1
# Reglas del negocio
# =====================================

from motor.politicas import *


def validar_edad(edad):

    if edad >= EDAD_MINIMA:
        return True, ""

    return False, f"La edad mínima es {EDAD_MINIMA} años."


def validar_ingreso(ingreso):

    if ingreso >= INGRESO_MINIMO:
        return True, ""

    return False, f"El ingreso líquido mínimo es S/ {INGRESO_MINIMO}."


def validar_contrato(contrato):

    if contrato in CONTRATOS_VALIDOS:
        return True, ""

    return False, "El tipo de contrato no es válido."


def validar_antiguedad(contrato, antiguedad):

    contrato = contrato.lower()

    if contrato in ["nombrado", "indeterminado", "indefinido", "cas indeterminado"]:

        if antiguedad >= 6:
            return True, ""

        return False, "Debe tener mínimo 6 meses de antigüedad."

    if contrato == "ley servir":

        if antiguedad >= 12:
            return True, ""

        return False, "Ley Servir requiere mínimo 12 meses."

    return False, "Contrato no reconocido."


def validar_entidades(entidades):

    if entidades <= MAX_ENTIDADES:
        return True, ""

    return False, f"No puede tener más de {MAX_ENTIDADES} entidades financieras."


def validar_perdidas(perdidas):

    if perdidas <= MAX_PERDIDAS:
        return True, ""

    return False, f"No puede tener más de {MAX_PERDIDAS} entidades en pérdida."


def validar_institucion(institucion, porta_arma):

    institucion = institucion.upper()

    if institucion in INSTITUCIONES_RESTRINGIDAS:

        if institucion == "PNP":

            if porta_arma.lower() == "sí" or porta_arma.lower() == "si":
                return False, "Personal armado de la PNP no es elegible."

        else:

            return False, f"La institución {institucion} no es atendida."

    return True, ""