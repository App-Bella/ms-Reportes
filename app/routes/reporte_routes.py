from flask import Blueprint, send_file
from app.pdf.generador_pdf import generar_pdf_prueba, generar_pdf_financiero
from app.services.reporte_service import obtener_datos_financieros

reporte_bp = Blueprint('reporte', __name__)

@reporte_bp.route('/prueba', methods=['GET'])
def reporte_prueba():
    ruta = generar_pdf_prueba()
    return send_file(ruta, as_attachment=True)

@reporte_bp.route('/financiero', methods=['GET'])
def reporte_financiero():
    datos = obtener_datos_financieros()
    ruta = generar_pdf_financiero(datos)
    return send_file(ruta, as_attachment=True)