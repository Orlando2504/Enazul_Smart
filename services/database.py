import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_DIR = BASE_DIR / "database"

DATABASE_DIR.mkdir(exist_ok=True)

DB_PATH = DATABASE_DIR / "enazul.db"


def get_connection():

    conn = sqlite3.connect(str(DB_PATH))

    conn.row_factory = sqlite3.Row

    return conn


def crear_base_datos():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS solicitudes (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            nombre TEXT,

            documento TEXT,

            celular TEXT,

            correo TEXT,

            institucion TEXT,

            contrato TEXT,

            antiguedad INTEGER,

            ingreso REAL,

            edad INTEGER,

            entidades INTEGER,

            perdidas INTEGER,

            porta_arma TEXT,

            estado TEXT,

            score INTEGER,

            riesgo TEXT

        )
    """)

    conn.commit()
    conn.close()

def guardar_solicitud(datos):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO solicitudes(

            nombre,
            documento,
            celular,
            correo,
            institucion,
            contrato,
            antiguedad,
            ingreso,
            edad,
            entidades,
            perdidas,
            porta_arma,
            estado,
            score,
            riesgo

        )

        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)

    """, (

        datos["nombre"],
        datos["documento"],
        datos["celular"],
        datos["correo"],
        datos["institucion"],
        datos["contrato"],
        datos["antiguedad"],
        datos["ingreso"],
        datos["edad"],
        datos["entidades"],
        datos["perdidas"],
        datos["porta_arma"],
        datos["estado"],
        datos["score"],
        datos["riesgo"]

    ))

    conn.commit()

    conn.close()