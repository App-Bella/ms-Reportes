import requests
from app.config.config import Config

def obtener_datos_financieros():
    """Consulta a MS-Analitica para traer el resumen financiero"""
    try:
        respuesta = requests.get(f"{Config.ANALITICA_URL}/analitica/financiero")
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con MS-Analitica: {e}")
        return []