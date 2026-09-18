from flask import Blueprint, send_file
from app.pdf.generador_pdf import generar_pdf_prueba

reporte_bp = Blueprint('reporte', __name__)

@reporte_bp.route('/prueba', methods=['GET'])
def reporte_prueba():
    ruta = generar_pdf_prueba()
    return send_file(ruta, as_attachment=True)