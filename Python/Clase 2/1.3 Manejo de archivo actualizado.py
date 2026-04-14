#Declaramos una variable utilizando el metodo open
try:
    archivo = open('prueba.txt', 'w') #La w es de write
    archivo.write("Las letras sirven para varias cosas\n ")
    archivo.write("por ej: acción, ejecución y producción\n ")
    archivo.write("las letras son: \nr read leer, \n a append anexa, \n w write escribe, \n x crea un archivo")
    archivo.write("\n t esta para texto o text, \n b archivos binarios, \n w+ lee y escribe")

except Exception as e:
    print(e)
finally: #siempre se va a ejecutar
    archivo.close() # se cierra el archivo
#Por mas que el archivo no exista, se va a crear y quedará en el directorio del projecto.
