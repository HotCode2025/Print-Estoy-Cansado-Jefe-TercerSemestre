import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'super_secret_key_simpsons' # Necesario para guardar la sesión del usuario

# Nuestras preguntas en código
preguntas = [
    {
        'id': 0,
        'texto': '¿Cuántos integrantes tiene la familia Simpson?',
        'opciones': ['3', '4', '5', '6'],
        'correcta': 2, # Índice de la respuesta '5'
        'puntos': 10
    },
    {
        'id': 1,
        'texto': '¿Cómo se llama el jefe de Homero?',
        'opciones': ['Ned Flanders', 'Montgomery Burns', 'Moe Szyslak', 'Waylon Smithers'],
        'correcta': 1, # Índice de la respuesta 'Montgomery Burns'
        'puntos': 15
    }
]

def init_db():
    conn = sqlite3.connect('trivia.db')
    cursor = conn.cursor()
    # Tabla de usuarios y progreso
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            puntaje INTEGER DEFAULT 0,
            pregunta_actual INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

# Inicia la DB
init_db()

@app.route('/', methods=['GET'])
def index():
    if 'usuario' in session:
        return redirect(url_for('jugar'))
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    conn = sqlite3.connect('trivia.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Buscamos si existe el user y la contra
    user = cursor.execute('SELECT * FROM usuarios WHERE username = ? AND password = ?', (username, password)).fetchone()
    
    if user:
        # Si existe y la contra es correcta
        session['usuario'] = user['username']
    else:
        # Si no existe, se crea directo
        try:
            cursor.execute('INSERT INTO usuarios (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            session['usuario'] = username
        except sqlite3.IntegrityError:
            # Si el username existe pero la contraseña estaba mal
            conn.close()
            return "Contraseña incorrecta. <a href='/'>Volver</a>"
            
    conn.close()
    return redirect(url_for('jugar'))

@app.route('/jugar', methods=['GET', 'POST'])
def jugar():
    if 'usuario' not in session:
        return redirect(url_for('index'))
        
    conn = sqlite3.connect('trivia.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    user = cursor.execute('SELECT * FROM usuarios WHERE username = ?', (session['usuario'],)).fetchone()
    pregunta_idx = user['pregunta_actual']
    puntaje = user['puntaje']
    
    # Procesar respuesta si viene por POST
    mensaje = None
    if request.method == 'POST':
        if 'guardar_salir' in request.form:
            conn.close()
            session.pop('usuario', None)
            return redirect(url_for('index'))
            
        respuesta_elegida = int(request.form.get('respuesta'))
        pregunta_actual = preguntas[pregunta_idx]
        
        if respuesta_elegida == pregunta_actual['correcta']:
            puntaje += pregunta_actual['puntos']
            mensaje = "¡Correcto!"
        else:
            mensaje = "¡Incorrecto!"
            
        pregunta_idx += 1 # Avanza a la siguiente
        
        # Guardar progreso en DB
        cursor.execute('UPDATE usuarios SET puntaje = ?, pregunta_actual = ? WHERE username = ?', 
                       (puntaje, pregunta_idx, session['usuario']))
        conn.commit()

    conn.close()
    
    # Comprobar si gano
    if pregunta_idx >= len(preguntas):
        return render_template('jugar.html', terminado=True, puntaje=puntaje)
        
    return render_template('jugar.html', pregunta=preguntas[pregunta_idx], puntaje=puntaje, mensaje=mensaje, terminado=False)

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
