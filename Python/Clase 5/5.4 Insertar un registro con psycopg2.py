import psycopg2 #Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(user="postgres", password="admin", host="127.0.0.1", port="5432", database="test_bd")
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "INSERT INTO persona (nombre, apellido, email)VALUES (%s, %s, %s)"
            valores = ("Carlos", "Lara", "clara@gmail.com") #esto es una tupla
            # conexion.commit() esto se utiliza para guardar los cambiso en la base de datos
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall()
            for registo in registros:
                print(registo)

except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close()
