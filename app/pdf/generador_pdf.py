from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generar_pdf_prueba():
    ruta = os.path.join("output", "reporte_prueba.pdf")
    c = canvas.Canvas(ruta, pagesize=letter)

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, 750, "Ponte Bella - Reporte de Prueba")

    c.setFont("Helvetica", 12)
    c.drawString(50, 700, "Este es un PDF generado con ReportLab")

    c.save()
    return ruta