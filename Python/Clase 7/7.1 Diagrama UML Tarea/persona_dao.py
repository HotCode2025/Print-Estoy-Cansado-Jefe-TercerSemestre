from conexion import Conexion
from persona import Persona


class PersonaDao:
    # Sentencias SQL
    __SELECCIONAR = "SELECT id_persona, nombre, apellido, email FROM persona"
    __INSERTAR    = "INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)"
    __ACTUALIZAR  = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s"
    __ELIMINAR    = "DELETE FROM persona WHERE id_persona=%s"
 
    @classmethod
    def seleccionar(cls) -> list[Persona]:
        """Retorna una lista con todos los registros de la tabla persona."""
        cursor = Conexion.obtenerCursor()
        cursor.execute(cls.__SELECCIONAR)
        registros = cursor.fetchall()
        personas = [
            Persona(r[0], r[1], r[2], r[3]) for r in registros
        ]
        return personas
 
    @classmethod
    def insertar(cls, cls_persona: Persona) -> int:
        """Inserta una nueva persona y retorna el número de filas afectadas."""
        cursor = Conexion.obtenerCursor()
        valores = (
            cls_persona.get_nombre(),
            cls_persona.get_apellido(),
            cls_persona.get_email(),
        )
        cursor.execute(cls.__INSERTAR, valores)
        Conexion.obtenerConexion().commit()
        return cursor.rowcount
 
    @classmethod
    def actualizando(cls, cls_persona: Persona) -> int:
        """Actualiza los datos de una persona y retorna el número de filas afectadas."""
        cursor = Conexion.obtenerCursor()
        valores = (
            cls_persona.get_nombre(),
            cls_persona.get_apellido(),
            cls_persona.get_email(),
            cls_persona.get_id_persona(),
        )
        cursor.execute(cls.__ACTUALIZAR, valores)
        Conexion.obtenerConexion().commit()
        return cursor.rowcount
 
    @classmethod
    def eliminar(cls, ccls_persona: Persona) -> int:
        """Elimina una persona por su id y retorna el número de filas afectadas."""
        cursor = Conexion.obtenerCursor()
        valores = (ccls_persona.get_id_persona(),)
        cursor.execute(cls.__ELIMINAR, valores)
        Conexion.obtenerConexion().commit()
        return cursor.rowcount
 
    # Ejemplo de uso

if __name__ == "__main__":
    # Insertar
    nueva = Persona(nombre="Ana", apellido="López", email="ana@mail.com")
    filas = PersonaDao.insertar(nueva)
    print(f"Filas insertadas: {filas}")
 
    # Seleccionar
    personas = PersonaDao.seleccionar()
    for p in personas:
        print(p)
 
    # Actualizar (asumiendo id=1)
    editar = Persona(id_persona=1, nombre="Ana", apellido="García", email="ana@mail.com")
    filas = PersonaDao.actualizando(editar)
    print(f"Filas actualizadas: {filas}")
 
    # Eliminar (asumiendo id=1)
    borrar = Persona(id_persona=1)
    filas = PersonaDao.eliminar(borrar)
    print(f"Filas eliminadas: {filas}")
 
    Conexion.cerrar()