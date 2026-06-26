import sqlite3

def init_db():
    # Conectarse a la base de datos
    conexion = sqlite3.connect('database/trivia.db')
    
    # Leer el script SQL (solo para crear las tablas)
    with open('database/schema.sql', 'r', encoding='utf-8') as f:
        schema = f.read()
        
    # Ejecutar el script SQL
    cursor = conexion.cursor()
    cursor.executescript(schema)
    
    # Guardar los cambios y cerrar
    conexion.commit()
    conexion.close()
    print("Base de datos inicializada correctamente.")

if __name__ == '__main__':
    init_db()
