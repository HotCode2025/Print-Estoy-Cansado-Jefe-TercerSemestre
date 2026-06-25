#Migramos usando dataclass para simplificar, "fusionamos" con la clase Respuesta del otro proyecto
from dataclasses import dataclass, field

@dataclass
class Pregunta:
    id: int
    texto: str
    #Dependiendo de como vayamos a estructurar las respuestas en la BBDD
    #opciones: list[str] = field(default_factory=list)
    opcion1: str
    opcion2: str
    opcion3: str
    opcion4: str
    indice_correcto: int

