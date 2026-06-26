import os
import sqlite3
from flask import Flask, render_template
from models.Pregunta import Pregunta, preguntas_trivia

app = Flask(__name__)

def get_db_connection():
    # Conectar a la base de datos
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
def jugar(pregunta_id=0):
    pregunta_obj = None
    
    # Buscar si el ID está dentro del rango de nuestra lista
    if 0 <= pregunta_id < len(preguntas_trivia):
        pregunta_obj = preguntas_trivia[pregunta_id]
        siguiente_id = pregunta_id + 1
    else:
        siguiente_id = None # Terminó el juego
        
    return render_template("jugar.html", pregunta=pregunta_obj, siguiente_id=siguiente_id)

if __name__ == "__main__":
    app.run(debug=True)