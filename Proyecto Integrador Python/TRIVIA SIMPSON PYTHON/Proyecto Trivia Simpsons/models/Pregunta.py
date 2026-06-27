from dataclasses import dataclass

@dataclass
class Pregunta:
    id: int
    texto: str
    opcion1: str
    opcion2: str
    opcion3: str
    opcion4: str
    indice_correcto: int

    @staticmethod
    def mapear_desde_bd(row):
        """
        Toma una fila (Row) de SQLite y la convierte en un objeto Pregunta.
        Esto evita mapear los datos a mano en las rutas de Flask.
        """
        if row is None:
            return None
        return Pregunta(
            id=row['id'],
            texto=row['texto'],
            opcion1=row['opcion1'],
            opcion2=row['opcion2'],
            opcion3=row['opcion3'],
            opcion4=row['opcion4'],
            indice_correcto=row['indice_correcto']
        )