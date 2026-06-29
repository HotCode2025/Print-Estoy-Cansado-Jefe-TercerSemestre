import os
import sqlite3
import time
from flask import Flask, render_template, session, request, redirect, url_for, flash
from models import Pregunta, Partida


app = Flask(__name__)
app.secret_key = 'clave_secreta_super_oculta_de_los_simpson'

LIMITE_TIEMPO = 600  # 10 minutos

def get_db_connection():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'database', 'trivia.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def inicio():
    conn = get_db_connection()
    top_jugadores = conn.execute("SELECT id, nombre_jugador, puntaje FROM ranking ORDER BY puntaje DESC LIMIT 10").fetchall()
    conn.close()
    top_jugadores = [Partida.mapear_desde_bd(jugador) for jugador in top_jugadores]
    return render_template("index.html", jugadores=top_jugadores)

@app.route("/registro", methods=["POST"])
def registro():
    nombre = request.form.get("nombre")
    if not nombre:
        flash("Por favor, ingresa un nombre.")
        return redirect(url_for('inicio'))
        
    conn = get_db_connection()
    try:
        cursor = conn.execute("INSERT INTO ranking (nombre_jugador, puntaje) VALUES (?, 0)", (nombre,))
        conn.commit()
        jugador_id = cursor.lastrowid
        session['jugador_id'] = jugador_id
        session['jugador_nombre'] = nombre
        session['puntaje'] = 0
        session['vidas'] = 3
        session['tiempo_inicio'] = time.time()  # Arranca el cronómetro al registrarse
    except sqlite3.IntegrityError:
        flash("Ese nombre ya está en uso. Por favor, elige otro.")
        return redirect(url_for('inicio'))
    finally:
        conn.close()
        
    return redirect(url_for('jugar'))


@app.route("/jugar", methods=["GET", "POST"])
@app.route("/jugar/<int:pregunta_id>", methods=["GET", "POST"])
def jugar(pregunta_id=None):
    if 'jugador_id' not in session:
        flash("Debes registrarte antes de jugar.")
        return redirect(url_for('inicio'))

    # Chequea si se acabó el tiempo
    tiempo_inicio = session.get('tiempo_inicio')
    if tiempo_inicio:
        transcurrido = time.time() - tiempo_inicio
        if transcurrido >= LIMITE_TIEMPO:
            puntaje_final = session.get('puntaje', 0)
            session.clear()
            flash(f"¡Se acabó el tiempo! Tu puntaje final fue {puntaje_final}.", "error")
            return redirect(url_for('inicio'))

    conn = get_db_connection()
    
    if request.method == "POST":
        opcion_elegida = int(request.form.get("opcion"))
        pregunta_actual_id = int(request.form.get("pregunta_id"))
        
        fila_pregunta = conn.execute("SELECT * FROM preguntas WHERE id = ?", (pregunta_actual_id,)).fetchone()
        pregunta_obj = Pregunta.mapear_desde_bd(fila_pregunta)
        
        if opcion_elegida == pregunta_obj.indice_correcto:
            if pregunta_actual_id <= 5:
                puntos = 50
            elif pregunta_actual_id <= 10:
                puntos = 100
            elif pregunta_actual_id <= 15:
                puntos = 150
            else:
                puntos = 200
                
            session['puntaje'] += puntos
            conn.execute("UPDATE ranking SET puntaje = ? WHERE id = ?", (session['puntaje'], session['jugador_id']))
            conn.commit()
            
            if pregunta_actual_id in [5, 10, 15]:
                niveles = {5: "Medio", 10: "Difícil", 15: "Fan"}
                flash(f"¡Subiste de Nivel! Ahora estás en nivel {niveles[pregunta_actual_id]}.", "levelup")
        else:
            session['vidas'] -= 1
            
        if session['vidas'] <= 0:
            conn.close()
            puntaje_final = session.get('puntaje', 0)
            session.clear()
            flash(f"¡Te quedaste sin vidas! Tu puntaje final fue {puntaje_final}.", "error")
            return redirect(url_for('inicio'))
            
        siguiente_registro = conn.execute("SELECT id FROM preguntas WHERE id > ? ORDER BY id ASC LIMIT 1", (pregunta_actual_id,)).fetchone()
        if siguiente_registro:
            conn.close()
            return redirect(url_for('jugar', pregunta_id=siguiente_registro['id']))
        else:
            conn.close()
            puntaje_final = session.get('puntaje', 0)
            session.clear()
            flash(f"¡Completaste todas las preguntas! Tu puntaje final fue {puntaje_final}.", "success")
            return redirect(url_for('inicio'))

    if pregunta_id is None:
        primer_registro = conn.execute("SELECT id FROM preguntas ORDER BY id ASC LIMIT 1").fetchone()
        if primer_registro:
            pregunta_id = primer_registro['id']
        else:
            conn.close()
            return render_template("jugar.html", pregunta=None, siguiente_id=None)
            
    fila_pregunta = conn.execute("SELECT * FROM preguntas WHERE id = ?", (pregunta_id,)).fetchone()
    pregunta_obj = Pregunta.mapear_desde_bd(fila_pregunta)
    
    siguiente_registro = conn.execute("SELECT id FROM preguntas WHERE id > ? ORDER BY id ASC LIMIT 1", (pregunta_id,)).fetchone()
    siguiente_id = siguiente_registro['id'] if siguiente_registro else None

    conn.close()

    # Calcula el tiempo restante para pasarlo al HTML
    transcurrido = time.time() - session.get('tiempo_inicio', time.time())
    tiempo_restante = max(0, LIMITE_TIEMPO - transcurrido)
    
    return render_template("jugar.html", pregunta=pregunta_obj, siguiente_id=siguiente_id, tiempo_restante=int(tiempo_restante))

@app.route("/salir", methods=["POST"])
def salir():
    session.clear()
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True)