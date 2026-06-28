import os
import sqlite3
from flask import Flask, render_template, session 
from models.Pregunta import Pregunta

app = Flask(__name__)
app.secret_key = 'clave_secreta_super_oculta_de_los_simpson'

def get_db_connection():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'database', 'trivia.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/jugar")
@app.route("/jugar/<int:pregunta_id>")
def jugar(pregunta_id=None):
    conn = get_db_connection()
    
    # Buscar la primera pregunta si no viene ID
    if pregunta_id is None:
        primer_registro = conn.execute("SELECT id FROM preguntas ORDER BY id ASC LIMIT 1").fetchone()
        if primer_registro:
            pregunta_id = primer_registro['id']
        else:
            return render_template("jugar.html", pregunta=None, siguiente_id=None)
            
    #Traer la fila de la BD
    fila_pregunta = conn.execute("SELECT * FROM preguntas WHERE id = ?", (pregunta_id,)).fetchone()
    
    #Convertimos la fila en un Objeto Pregunta
    pregunta_obj = Pregunta.mapear_desde_bd(fila_pregunta)
    
    #Buscar el ID de la siguiente pregunta
    siguiente_registro = conn.execute("SELECT id FROM preguntas WHERE id > ? ORDER BY id ASC LIMIT 1", (pregunta_id,)).fetchone()
    siguiente_id = siguiente_registro['id'] if siguiente_registro else None

    conn.close()
    
    return render_template("jugar.html", pregunta=pregunta_obj, siguiente_id=siguiente_id)
@app.route("/salir")
def salir():
    session.clear()
    return render_template("despedida.html")
if __name__ == "__main__":
    app.run(debug=True)