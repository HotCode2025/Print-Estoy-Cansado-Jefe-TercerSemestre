#clase Partida, usamos dataclass para optimizar el codigo migrado desde Java
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Partida:
    id: int | None
    nombre_jugador: str
    puntaje_obtenido: int
    fecha: datetime
