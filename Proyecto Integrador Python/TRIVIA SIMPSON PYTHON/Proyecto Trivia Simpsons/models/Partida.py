#clase Partida, usamos dataclass para optimizar el codigo migrado desde Java
from dataclasses import dataclass
from sqlite3 import Row

@dataclass
class Partida:
    id: int | None
    nombre_jugador: str
    puntaje: int

    @staticmethod
    def mapear_desde_bd(row: Row):
        return Partida(
            id=row["id"],
            nombre_jugador=row["nombre_jugador"],
            puntaje=row["puntaje"]
        )
    
