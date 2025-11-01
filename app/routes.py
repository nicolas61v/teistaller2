from flask import Blueprint, jsonify, render_template_string
import os
import socket
from .models import obtener_pokenea_aleatorio
import boto3

# Crear blueprint
bp = Blueprint('api', __name__)

def get_container_id():
    """Obtiene el ID del contenedor (hostname)"""
    try:
        return socket.gethostname()
    except:
        return "unknown"

def get_s3_image_url(filename):
    """Obtiene la URL pública de una imagen en S3 o usa la URL directa si es una URL completa"""
    # Si ya es una URL, devolverla tal cual
    if filename.startswith('http'):
        return filename

    # Si no, construir la URL de S3
    bucket_name = os.getenv('S3_BUCKET', 'pokeneas-bucket')
    region = os.getenv('AWS_REGION', 'us-east-1')
    return f"https://{bucket_name}.s3.{region}.amazonaws.com/{filename}"

@bp.route('/api/pokenea', methods=['GET'])
def pokenea_json():
    """Ruta que retorna un Pokenea aleatorio en JSON"""
    pokenea = obtener_pokenea_aleatorio()
    container_id = get_container_id()

    response = {
        "container_id": container_id,
        "pokenea": pokenea.to_dict()
    }

    return jsonify(response), 200

@bp.route('/pokenea', methods=['GET'])
def pokenea_html():
    """Ruta que muestra un Pokenea con su imagen y frase filosófica"""
    pokenea = obtener_pokenea_aleatorio()
    container_id = get_container_id()
    image_url = get_s3_image_url(pokenea.imagen)

    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pokenea - {pokenea.nombre}</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}

            body {{
                font-family: 'Arial', sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }}

            .container {{
                background: white;
                border-radius: 20px;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
                padding: 40px;
                max-width: 500px;
                text-align: center;
            }}

            .pokenea-image {{
                width: 300px;
                height: 300px;
                margin: 0 auto 30px;
                object-fit: contain;
                background: #f0f0f0;
                border-radius: 15px;
                padding: 10px;
            }}

            .pokenea-name {{
                font-size: 2.5em;
                color: #333;
                margin-bottom: 20px;
                font-weight: bold;
            }}

            .pokenea-info {{
                background: #f9f9f9;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 20px;
            }}

            .info-item {{
                margin: 10px 0;
                font-size: 1.1em;
                color: #555;
            }}

            .label {{
                font-weight: bold;
                color: #667eea;
            }}

            .quote {{
                background: #e8f4f8;
                border-left: 5px solid #667eea;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 20px;
                font-style: italic;
                color: #333;
                font-size: 1.1em;
                line-height: 1.6;
            }}

            .container-id {{
                background: #333;
                color: #00ff00;
                padding: 15px;
                border-radius: 10px;
                margin-top: 20px;
                font-family: 'Courier New', monospace;
                font-size: 0.9em;
                word-break: break-all;
            }}

            .refresh-btn {{
                background: #667eea;
                color: white;
                border: none;
                padding: 12px 30px;
                font-size: 1em;
                border-radius: 25px;
                cursor: pointer;
                transition: background 0.3s ease;
                margin-top: 20px;
            }}

            .refresh-btn:hover {{
                background: #764ba2;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <img src="{image_url}" alt="{pokenea.nombre}" class="pokenea-image" onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%22300%22 height=%22300%22%3E%3Crect fill=%22%23f0f0f0%22 width=%22300%22 height=%22300%22/%3E%3Ctext x=%2250%25%22 y=%2250%25%22 dominant-baseline=%22middle%22 text-anchor=%22middle%22 font-family=%22Arial%22 font-size=%2224%22 fill=%22%23999%22%3EImagen no disponible%3C/text%3E%3C/svg%3E'">

            <h1 class="pokenea-name">{pokenea.nombre}</h1>

            <div class="pokenea-info">
                <div class="info-item">
                    <span class="label">ID:</span> {pokenea.id}
                </div>
                <div class="info-item">
                    <span class="label">Altura:</span> {pokenea.altura}
                </div>
                <div class="info-item">
                    <span class="label">Habilidad:</span> {pokenea.habilidad}
                </div>
            </div>

            <div class="quote">
                "{pokenea.frase_filosofica}"
            </div>

            <button class="refresh-btn" onclick="location.reload()">Obtener otro Pokenea</button>

            <div class="container-id">
                ID del Contenedor: <br> {container_id}
            </div>
        </div>
    </body>
    </html>
    """

    return html, 200
