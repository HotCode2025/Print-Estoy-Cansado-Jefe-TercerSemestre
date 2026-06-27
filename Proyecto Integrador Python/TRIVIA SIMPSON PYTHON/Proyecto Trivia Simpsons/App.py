import os
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'database', 'trivia.db')
    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Esto nos permite acceder a las columnas por nombre como un diccionario
    return conn

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/jugar")
@app.route("/jugar/<int:pregunta_id>")
def jugar(pregunta_id=None):
    conn = get_db_connection()
    
    # 1. Si no viene un ID, buscamos la primera pregunta de la base de datos
    if pregunta_id is None:
        primer_registro = conn.execute("SELECT id FROM preguntas ORDER BY id ASC LIMIT 1").fetchone()
        if primer_registro:
            pregunta_id = primer_registro['id']
        else:
            return render_template("jugar.html", pregunta=None, siguiente_id=None)
            
    # 2. Buscar la pregunta actual por su ID
    pregunta_obj = conn.execute("SELECT * FROM preguntas WHERE id = ?", (pregunta_id,)).fetchone()
    
    # 3. Buscar el ID de la siguiente pregunta que exista en la BD (por si hay saltos de ID)
    siguiente_registro = conn.execute("SELECT id FROM preguntas WHERE id > ? ORDER BY id ASC LIMIT 1", (pregunta_id,)).fetchone()
    
    siguiente_id = siguiente_registro['id'] if siguiente_registro else None

    conn.close()
    
    return render_template("jugar.html", pregunta=pregunta_obj, siguiente_id=siguiente_id)

if __name__ == "__main__":
    app.run(debug=True)