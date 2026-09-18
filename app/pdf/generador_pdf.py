from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
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

def generar_pdf_financiero(datos):
    ruta = os.path.join("output", "reporte_financiero.pdf")
    doc = SimpleDocTemplate(ruta, pagesize=letter)
    estilos = getSampleStyleSheet()
    elementos = []

    elementos.append(Paragraph("Ponte Bella - Reporte Financiero", estilos['Title']))
    elementos.append(Spacer(1, 20))

    tabla_datos = [["Categoria", "Total"]]

    for item in datos:
        tabla_datos.append([item["categoria"], f"${item['total']:,}"])

    tabla = Table(tabla_datos, colWidths=[250, 150])
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#4A4A4A")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (1, 1), (1, -1), 'RIGHT'),
    ]))

    elementos.append(tabla)
    doc.build(elementos)
    return ruta

def generar_pdf_concurrencia(datos):
    ruta = os.path.join("output", "reporte_concurrencia.pdf")
    doc = SimpleDocTemplate(ruta, pagesize=letter)
    estilos = getSampleStyleSheet()
    elementos = []

    elementos.append(Paragraph("Ponte Bella - Reporte de Concurrencia", estilos['Title']))
    elementos.append(Spacer(1, 20))

    tabla_datos = [["Servicio", "Cantidad", "Valor"]]

    suma_total = 0
    for item in datos:
        servicio = item["servicio"] if item["servicio"] else "Sin especificar"
        valor = item.get("valor_total", 0)
        suma_total += valor
        tabla_datos.append([servicio, str(item["cantidad"]), f"${valor:,}"])

    # Fila final con el total general
    tabla_datos.append(["", "Total", f"${suma_total:,}"])

    tabla = Table(tabla_datos, colWidths=[200, 100, 150])
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#4A4A4A")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (1, 1), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor("#D9D9D9")),
    ]))

    elementos.append(tabla)
    doc.build(elementos)
    return ruta