from flask import Flask

def create_app():
    """Crear y configurar la aplicación Flask"""
    app = Flask(__name__)

    # Registrar blueprints
    from .routes import bp
    app.register_blueprint(bp)

    @app.route('/')
    def index():
        return """
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Pokenea - Inicio</title>
            <style>
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }

                body {
                    font-family: 'Arial', sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    padding: 20px;
                }

                .container {
                    background: white;
                    border-radius: 20px;
                    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
                    padding: 50px;
                    max-width: 600px;
                    text-align: center;
                }

                h1 {
                    font-size: 3em;
                    color: #333;
                    margin-bottom: 20px;
                }

                p {
                    font-size: 1.1em;
                    color: #666;
                    margin-bottom: 30px;
                    line-height: 1.6;
                }

                .buttons {
                    display: flex;
                    gap: 20px;
                    flex-wrap: wrap;
                    justify-content: center;
                }

                .btn {
                    padding: 15px 40px;
                    font-size: 1.1em;
                    border: none;
                    border-radius: 25px;
                    cursor: pointer;
                    transition: all 0.3s ease;
                    text-decoration: none;
                    display: inline-block;
                    font-weight: bold;
                }

                .btn-primary {
                    background: #667eea;
                    color: white;
                }

                .btn-primary:hover {
                    background: #764ba2;
                    transform: translateY(-2px);
                    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
                }

                .btn-secondary {
                    background: #f093fb;
                    color: white;
                }

                .btn-secondary:hover {
                    background: #f5576c;
                    transform: translateY(-2px);
                    box-shadow: 0 5px 15px rgba(245, 87, 108, 0.4);
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🎮 Pokenea</h1>
                <p>Descubre a los Pokeneas de Antioquia. Estos criaturas mágicas nacen en las montañas colombianas y poseen habilidades únicas.</p>

                <div class="buttons">
                    <a href="/pokenea" class="btn btn-primary">Ver Pokenea Visual</a>
                    <a href="/api/pokenea" class="btn btn-secondary">Ver Pokenea JSON</a>
                </div>
            </div>
        </body>
        </html>
        """

    return app
