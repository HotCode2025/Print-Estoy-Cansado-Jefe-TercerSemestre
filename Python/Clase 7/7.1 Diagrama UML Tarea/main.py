from conexion import Conexion
from persona import Persona
from persona_dao import PersonaDao

# INSERTAR 
nueva_persona = Persona(nombre="Ana", apellido="López", email="ana@mail.com")
filas = PersonaDao.insertar(nueva_persona)
print(f"Filas insertadas: {filas}")

# SELECCIONAR 
print("\nTodas las personas:")
personas = PersonaDao.seleccionar()
for p in personas:
    print(p)

# ACTUALIZAR
editar = Persona(id_persona=1, nombre="Ana", apellido="García", email="ana@mail.com")
filas = PersonaDao.actualizando(editar)
print(f"\nFilas actualizadas: {filas}")

# ELIMINAR
borrar = Persona(id_persona=1)
filas = PersonaDao.eliminar(borrar)
print(f"Filas eliminadas: {filas}")

# CERRAR CONEXIÓN 
Conexion.cerrar()
print("\nConexión cerrada.")