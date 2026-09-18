from flask import Flask
from app.config.config import Config
from app.routes.reporte_routes import reporte_bp

app = Flask(__name__)
app.register_blueprint(reporte_bp, url_prefix='/reportes')

@app.route('/')
def inicio():
    return {"mensaje": "MS-Reporte corriendo correctamente"}

if __name__ == '__main__':
    app.run(port=Config.PORT, debug=True)