from dataclasses import dataclass

@dataclass
class Solicitud:
    edad: int
    ingreso: float
    contrato: str
    institucion: str
    antiguedad: int
    entidades: int
    perdidas: int
    porta_arma: str