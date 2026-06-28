import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'super_secret_key_simpsons' # Necesario para guardar la sesión del usuario

# Nuestras preguntas en código
preguntas = [
    {
        'id': 0,
        'texto': '¿Cuántos miembros tiene la familia Simpson?',
        'opciones': ['5', '4', '7', '6'],
        'correcta': 0,  # Índice de la respuesta '5'
        'puntos': 10
    },
    {
        'id': 1,
        'texto': '¿Qué instrumento toca Lisa?',
        'opciones': ['Xilófono', 'Flauta', 'Saxofón', 'Piano'],
        'correcta': 2,  # Índice de la respuesta 'Saxofón'
        'puntos': 10
    },
    {
        'id': 2,
        'texto': '¿Cuál es el nombre del vecino religioso de los Simpson?',
        'opciones': ['Ned Flanders', 'Barney Gumble', 'Moe Szyslak', 'Apu Nahasapeemapetilon'],
        'correcta': 0,  # Índice de la respuesta 'Ned Flanders'
        'puntos': 10
    },
    {
        'id': 3,
        'texto': '¿De qué color es el vehículo de la familia?',
        'opciones': ['Rosado', 'Naranja', 'Celeste', 'Verde'],
        'correcta': 0,  # Índice de la respuesta 'Rosado'
        'puntos': 10
    },
    {
        'id': 4,
        'texto': '¿Cuáles son las tías de los hijos de Marge?',
        'opciones': ['Jacqueline Bouvier y Selma Bouvier', 'Selma Bouvier y Patty Bouvier', 'Lisa Bouvier y Edna Bouvier', 'Jacqueline Bouvier y Patty Bouvier'],
        'correcta': 1,  # Índice de la respuesta 'Selma Bouvier y Patty Bouvier'
        'puntos': 10
    },
    {
        'id': 5,
        'texto': '¿Cómo se llaman los bravucones de la escuela de Lisa y Bart?',
        'opciones': ['Milhouse, Martin, Todd, Rafa', 'Nelson, Jimbo, Kearny, Dolph', 'Apu, Moe, Skinner, Edna', 'Bart, Lisa, Maggie, Ralph'],
        'correcta': 1,  # Índice de la respuesta 'Nelson, Jimbo, Kearny, Dolph'
        'puntos': 15
    },
    {
        'id': 6,
        'texto': 'Completa la frase: «Nada puede...»',
        'opciones': ['Pasar', 'salir mal', 'Malir Sal', 'fallar'],
        'correcta': 2,  # Índice de la respuesta 'Malir Sal'
        'puntos': 15
    },
    {
        'id': 7,
        'texto': '¿Cuál es el nombre de los hijos de Ned Flanders?',
        'opciones': ['Rod', 'Haggley y Lisa', 'Jimbo y Nelson', 'Todd'],
        'correcta': 0,  # Índice de la respuesta 'Rod'
        'puntos': 15
    },
    {
        'id': 8,
        'texto': '¿Cómo se llama el payaso famoso de la televisión en Springfield?',
        'opciones': ['Bozo', 'Krusty', 'Bob Patiño', 'Gabbo'],
        'correcta': 1,  # Índice de la respuesta 'Krusty'
        'puntos': 15
    },
    {
        'id': 9,
        'texto': '¿Qué personaje dice frecuentemente «Excelente» juntando las dos dedos?',
        'opciones': ['Smithers', 'Mr. Burns', 'Kent Brockman', 'Lenny'],
        'correcta': 1,  # Índice de la respuesta 'Mr. Burns'
        'puntos': 15
    },
    {
        'id': 10,
        'texto': 'Sin televisión y sin cerveza, Homero qué pierde?',
        'opciones': ['Un Bat', 'La cabeza', 'Maggie', 'La paciencia'],
        'correcta': 1,  # Índice de la respuesta 'La cabeza'
        'puntos': 20
    },
    {
        'id': 11,
        'texto': '¿A quién ayuda Homero cuando está en problemas?',
        'opciones': ['Jebus', 'Batman', 'Superman', 'Barney'],
        'correcta': 0,  # Índice de la respuesta 'Jebus'
        'puntos': 20
    },
    {
        'id': 12,
        'texto': '¿Qué animal fue el ayudante de Jesús se hizo un plagio?',
        'opciones': ['Un Gorgojo', 'Un Hamster', 'Un sapo', 'Un perro'],
        'correcta': 2,  # Índice de la respuesta 'Un sapo'
        'puntos': 20
    },
    {
        'id': 13,
        'texto': '¿Qué tipo de pez tiene Bart en su acuario?',
        'opciones': ['Un Pez Globo', 'Un Pez León', 'Un Pez Payaso', 'Un Pez Dorado'],
        'correcta': 1,  # Índice de la respuesta 'Un Pez León'
        'puntos': 20
    },
    {
        'id': 14,
        'texto': '¿Cuántos hijos tiene Cletus?',
        'opciones': ['19', '27', '34', '15'],
        'correcta': 2,  # Índice de la respuesta '34'
        'puntos': 20
    },
    {
        'id': 15,
        'texto': '¿En qué regimiento sirvió Abraham Simpson?',
        'opciones': ['Crimson Stone Chasers', 'Flying Hellfish', 'Flying Hellhounds', 'Springfield Army'],
        'correcta': 1,  # Índice de la respuesta 'Flying Hellfish'
        'puntos': 25
    },
    {
        'id': 16,
        'texto': '¿En su juventud, de qué trabajaba Mona Simpson?',
        'opciones': ['Enfermera', 'Asistente', 'Activista', 'Maestra'],
        'correcta': 2,  # Índice de la respuesta 'Activista'
        'puntos': 25
    },
    {
        'id': 17,
        'texto': '¿Qué pasa con el billete de un billón de dólares del Sr. Burns?',
        'opciones': ['Lo recupera el FBI', 'Lo obtiene Fidel Castro', 'Se pierde en el agua', 'Lo roba Smithers'],
        'correcta': 1,  # Índice de la respuesta 'Lo obtiene Fidel Castro'
        'puntos': 25
    },
    {
        'id': 18,
        'texto': '¿Cuántas veces se ha casado Krusty?',
        'opciones': ['5', '37', '10', '2'],
        'correcta': 0,  # Índice de la respuesta '5'
        'puntos': 25
    },
    {
        'id': 19,
        'texto': '¿Cuál es el nombre del grupo musical universitario en el que estuvo el Director Skinner y qué instrumento tocaba?',
        'opciones': ['Captain Fantasy and the Soft-Touch Feelings + Bongo', 'Borbotones + Guitarra', 'Cypress Creek Mens Chorus + Violin', 'Springfield Jazz Band + Trompeta'],
        'correcta': 0,  # Índice de la respuesta 'Captain Fantasy and the Soft-Touch Feelings + Bongo'
        'puntos': 25
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
