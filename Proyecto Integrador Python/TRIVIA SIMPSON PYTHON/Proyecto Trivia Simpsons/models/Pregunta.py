#Migramos usando dataclass para simplificar, "fusionamos" con la clase Respuesta del otro proyecto
from dataclasses import dataclass, field

@dataclass
class Pregunta:
    id: int
    texto: str
    opcion1: str
    opcion2: str
    opcion3: str
    opcion4: str
    indice_correcto: int

# Lista de preguntas en memoria
preguntas_trivia = [
    Pregunta(
        id=0,
        texto='¿Cuántos integrantes tiene la familia Simpson?',
        opcion1='3',
        opcion2='4',
        opcion3='5',
        opcion4='6',
        indice_correcto=2 # La opción '5' es la correcta, índice 2 (si pensamos 0, 1, 2, 3) o índice 3 si es base 1. Lo dejamos en 3 para que sea opción 3.
    ),
    Pregunta(
        id=1,
        texto='¿Cómo se llama el jefe de Homero?',
        opcion1='Ned Flanders',
        opcion2='Montgomery Burns',
        opcion3='Moe Szyslak',
        opcion4='Waylon Smithers',
        indice_correcto=2
    )
]
