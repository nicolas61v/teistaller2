import random
import os

class Pokenea:
    """Clase que representa un Pokenea de Antioquia"""

    def __init__(self, id, nombre, altura, habilidad, imagen, frase_filosofica):
        self.id = id
        self.nombre = nombre
        self.altura = altura
        self.habilidad = habilidad
        self.imagen = imagen
        self.frase_filosofica = frase_filosofica

    def to_dict(self):
        """Convierte el Pokenea a un diccionario"""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "altura": self.altura,
            "habilidad": self.habilidad
        }


# Base de datos de Pokeneas (datos quemados)
POKENEAS = [
    Pokenea(
        id=1,
        nombre="Medellínchu",
        altura="0.5m",
        habilidad="Velocidad urbana",
        imagen="pokeneas/pokenea1.png",
        frase_filosofica="En la montaña de la vida, la constancia es el camino."
    ),
    Pokenea(
        id=2,
        nombre="Arequero",
        altura="0.6m",
        habilidad="Precisión",
        imagen="pokeneas/pokenea2.png",
        frase_filosofica="Quien dispara con intención, alcanza sus metas."
    ),
    Pokenea(
        id=3,
        nombre="Cafetolina",
        altura="0.4m",
        habilidad="Energía infinita",
        imagen="pokeneas/pokenea3.png",
        frase_filosofica="Cada taza de café es una nueva oportunidad."
    ),
    Pokenea(
        id=4,
        nombre="Valledupar",
        altura="0.7m",
        habilidad="Ritmo perfecto",
        imagen="pokeneas/pokenea4.png",
        frase_filosofica="La vida es una cumbia, ¡hay que bailarla!"
    ),
    Pokenea(
        id=5,
        nombre="Santandereño",
        altura="0.65m",
        habilidad="Fuerza ancestral",
        imagen="pokeneas/pokenea5.png",
        frase_filosofica="Desde las montañas, la sabiduría nos guía."
    ),
    Pokenea(
        id=6,
        nombre="Chocoano",
        altura="0.55m",
        habilidad="Control del agua",
        imagen="pokeneas/pokenea6.png",
        frase_filosofica="El río enseña que todo fluye hacia adelante."
    ),
    Pokenea(
        id=7,
        nombre="Caribeño",
        altura="0.6m",
        habilidad="Calor tropical",
        imagen="pokeneas/pokenea7.png",
        frase_filosofica="Con el sol y la brisa, todo es posible."
    ),
    Pokenea(
        id=8,
        nombre="Nariñense",
        altura="0.58m",
        habilidad="Teleportación andina",
        imagen="pokeneas/pokenea8.png",
        frase_filosofica="En las alturas, el espíritu se libera."
    ),
    Pokenea(
        id=9,
        nombre="Tolimense",
        altura="0.62m",
        habilidad="Resistencia al calor",
        imagen="pokeneas/pokenea9.png",
        frase_filosofica="El calor templa al alma como el acero."
    ),
    Pokenea(
        id=10,
        nombre="Quindiano",
        altura="0.5m",
        habilidad="Cosecha de sueños",
        imagen="pokeneas/pokenea10.png",
        frase_filosofica="Cada grano de café es un sueño plantado."
    ),
]

def obtener_pokenea_aleatorio():
    """Retorna un Pokenea aleatorio"""
    return random.choice(POKENEAS)