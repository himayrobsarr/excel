from flask import Flask
from routes.excelRoutes import excel_blueprint

app = Flask(__name__)

# Registrar rutas
# Registramos el blueprint de excel con el prefijo /excel para todas sus rutas
app.register_blueprint(excel_blueprint, url_prefix="/excel")

# Si este archivo se ejecuta directamente (no se importa como módulo)
# iniciamos el servidor Flask en modo debug
if __name__ == '__main__':
    app.run(debug=True)