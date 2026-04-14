# Declaramos una variable
try:
    archivo = open('prueba.txt', 'w', encoding='utf8')  # La w es de write que significa escribir
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('como por ejemplo: acción, ejecución y producción\n')
    archivo.write('las letras son:\n')
    archivo.write('r read leer,\n')
    archivo.write('a append anexa,\n')
    archivo.write('w write escribe,\n')
    archivo.write('x crea un archivo\n')
    archivo.write('t esta es para texto o text,\n')
    archivo.write('b archivos binarios,\n')
    archivo.write('w+ lee y escribe son igules r+\n')
    archivo.write('Saludos a todos los alumnos de la tecnicatura\n')
    archivo.write('Con esto terminamos\n')
except Exception as e:
    print(e)
finally:  # siempre se ejecuta
    archivo.close()  # Con esto se debe cerrar el archivo
# archivo.write('Todo quedo perfecto'): este es un error