import os
from dotenv import load_dotenv
from app import create_app

# Cargar variables de entorno
load_dotenv()

# Crear la aplicación
app = create_app()

if __name__ == '__main__':
    # La aplicación debe escuchar en 0.0.0.0 para funcionar en Docker
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=os.getenv('DEBUG', 'False') == 'True')
