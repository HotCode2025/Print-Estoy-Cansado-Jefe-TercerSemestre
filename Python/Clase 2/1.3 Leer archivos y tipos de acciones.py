archivo = open('prueba.txt', 'r', encoding='utf8') #según la letras cambia lo que hace con el archivo

#archivo = open('prueba.txt', 'r', encoding='utf8') - read
#archivo = open('prueba.txt', 'a', encoding='utf8') - append
#archivo = open('prueba.txt', 'w', encoding='utf8') - write
#archivo = open('prueba.txt', 'x', encoding='utf8') - lanza exception

print(archivo.read())
