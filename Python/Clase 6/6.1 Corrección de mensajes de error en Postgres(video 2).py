import psycopg2

# Si cambiamos `user='postgres'` por `user='postgres1'`, ocurre un error detallado (OperationalError)
# porque PostgreSQL tiene su propio sistema de usuarios y permisos (Roles) independiente de Windows.
# El motor de la base de datos busca si existe el usuario 'postgres1', al no encontrarlo 
# (o si la contraseña no coincide), el propio servidor de Postgres rechaza la conexión
# y le devuelve a Python un mensaje "FATAL" con los detalles exactos del porqué falló.
conexion = psycopg2.connect(user='postgres1', password='admin', host='127.0.0.1', port='5432', database='test_bd')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona=%s'
            id_persona = input('Digite un id para la búsqueda: ')
            cursor.execute(sentencia, (id_persona,))
            registros = cursor.fetchone()
            print(registros)

except Exception as e:
    print(f'Ocurrió un error: {e}')

finally:
    conexion.close()

# https://www.psycopg.org/docs/usage.html