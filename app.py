from flask import Flask
from routes.inicio import inicio_bp
from routes.formulario import formulario_bp
from services.database import crear_base_datos

app = Flask(__name__)

crear_base_datos()

# Registrar rutas
app.register_blueprint(inicio_bp)
app.register_blueprint(formulario_bp)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )