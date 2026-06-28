DROP TABLE IF EXISTS ranking;

DROP TABLE IF EXISTS preguntas;

-- Tabla de preguntas de la trivia
CREATE TABLE preguntas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    texto TEXT NOT NULL,
    opcion1 TEXT NOT NULL,
    opcion2 TEXT NOT NULL,
    opcion3 TEXT NOT NULL,
    opcion4 TEXT NOT NULL,
    indice_correcto INTEGER NOT NULL
);

-- Tabla de ranking/partidas
CREATE TABLE ranking (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_jugador TEXT NOT NULL UNIQUE,
    puntaje INTEGER NOT NULL DEFAULT 0,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- NIVEL FÁCIL (Preguntas 1 a 5)
INSERT INTO
    preguntas (
        texto,
        opcion1,
        opcion2,
        opcion3,
        opcion4,
        indice_correcto
    )
VALUES (
        '¿Cuántos miembros tiene la familia Simpson?',
        '5',
        '4',
        '7',
        '6',
        0
    );

INSERT INTO
    preguntas (
        texto,
        opcion1,
        opcion2,
        opcion3,
        opcion4,
        indice_correcto
    )
VALUES (
        '¿Qué instrumento toca Lisa?',
        'Xilófono',
        'Flauta',
        'Saxofón',
        'Piano',
        2
    );

INSERT INTO
    preguntas (
        texto,
        opcion1,
        opcion2,
        opcion3,
        opcion4,
        indice_correcto
    )
VALUES (
        '¿Cuál es el nombre del vecino religioso de los Simpson?',
        'Ned Flanders',
        'Barney Gumble',
        'Moe Szyslak',
        'Apu Nahasapeemapetilon',
        0
    );

INSERT INTO
    preguntas (
        texto,
        opcion1,
        opcion2,
        opcion3,
        opcion4,
        indice_correcto
    )
VALUES (
        '¿De qué color es el vehículo principal de la familia?',
        'Rosado',
        'Naranja',
        'Celeste',
        'Verde',
        0
    );

INSERT INTO
    preguntas (
        texto,
        opcion1,
        opcion2,
        opcion3,
        opcion4,
        indice_correcto
    )
VALUES (
        '¿Cuáles son los nombres de las hermanas de Marge?',
        'Jacqueline y Selma',
        'Selma y Patty',
        'Lisa y Edna',
        'Jacqueline y Patty',
        1
    );

-- NIVEL MEDIO (Preguntas 6 a 10)
INSERT INTO
    preguntas (
        texto,
        opcion1,
        opcion2,
        opcion3,
        opcion4,
        indice_correcto
    )
VALUES (
        '¿Cómo se llaman los bravucones de la escuela primaria de Springfield?',
        'Milhouse, Martin, Todd, Rafa',
        'Nelson, Jimbo, Kearny, Dolph',
        'Apu, Moe, Skinner, Edna',
        'Bart, Lisa, Maggie, Ralph',
        1
    );

INSERT INTO
    preguntas (
        texto,
        opcion1,
        opcion2,
        opcion3,
        opcion4,
        indice_correcto
    )
VALUES (
        'Completa la famosa frase: «Nada puede...»',
        'Pasar',
        'salir mal',
        'Malir Sal',
        'fallar',
        2
    );

INSERT INTO
    preguntas (
        texto,
        opcion1,
        opcion2,
        opcion3,
        opcion4,
        indice_correcto
    )
VALUES (
        '¿Cuáles son los nombres de los hijos de Ned Flanders?',
        'Rod y Todd',
        'Haggley y Lisa',
        'Jimbo y Nelson',
        'Bart y Milhouse',
        0
    );

INSERT INTO
    preguntas (
        texto,
        opcion1,
        opcion2,
        opcion3,
        opcion4,
        indice_correcto
    )
VALUES (
        '¿Cómo se llama el payaso más famoso de la televisión en Springfield?',
        'Bozo',
        'Krusty',
        'Bob Patiño',
        'Gabbo',
        1
    );

INSERT INTO
    preguntas (
        texto,
        opcion1,
        opcion2,
        opcion3,
        opcion4,
        indice_correcto
    )
VALUES (
        '¿Qué personaje dice frecuentemente «Excelente» juntando los dedos de sus manos?',
        'Smithers',
        'Mr. Burns',
        'Kent Brockman',
        'Lenny',
        1
    );

-- NIVEL DIFÍCIL (Preguntas 11 a 15)
INSERT INTO
    preguntas (
        texto,
        opcion1,
        opcion2,
        opcion3,
        opcion4,
        indice_correcto
    )
VALUES (
        'Completa: «Sin televisión y sin cerveza, Homero pierde...»',
        'Un Bat',
        'La cabeza',
        'A Maggie',
        'La paciencia',
        1
    );

INSERT INTO
    preguntas (
        texto,
        opcion1,
        opcion2,
        opcion3,
        opcion4,
        indice_correcto
    )
VALUES (
        '¿A quién le pide ayuda Homero desesperadamente cuando está en problemas?',
        'Jebús',
        'Batman',
        'Superman',
        'Barney',
        0
    );

INSERT INTO
    preguntas (
        texto,
        opcion1,
        opcion2,
        opcion3,
        opcion4,
        indice_correcto
    )
VALUES (
        'En el episodio de los misioneros, ¿qué animal introdujo Bart que se convirtió en una plaga?',
        'Un Gorgojo',
        'Un Hamster',
        'Un sapo',
        'Un perro',
        2
    );

INSERT INTO
    preguntas (
        texto,
        opcion1,
        opcion2,
        opcion3,
        opcion4,
        indice_correcto
    )
VALUES (
        '¿Qué tipo de pez peligroso tiene Bart en su acuario o inodoro?',
        'Un Pez Globo',
        'Un Pez León',
        'Un Pez Payaso',
        'Un Pez Dorado',
        1
    );

INSERT INTO
    preguntas (
        texto,
        opcion1,
        opcion2,
        opcion3,
        opcion4,
        indice_correcto
    )
VALUES (
        '¿Cuántos hijos tiene Cletus el granjero?',
        '19',
        '27',
        '34',
        '15',
        2
    );

-- NIVEL FAN (Preguntas 16 a 20)
INSERT INTO
    preguntas (
        texto,
        opcion1,
        opcion2,
        opcion3,
        opcion4,
        indice_correcto
    )
VALUES (
        '¿En qué escuadrón militar de la Segunda Guerra Mundial sirvió el Abuelo Simpson?',
        'Crimson Stone Chasers',
        'Flying Hellfish',
        'Flying Hellhounds',
        'Springfield Army',
        1
    );

INSERT INTO
    preguntas (
        texto,
        opcion1,
        opcion2,
        opcion3,
        opcion4,
        indice_correcto
    )
VALUES (
        'En su juventud, ¿a qué se dedicaba Mona Simpson?',
        'Enfermera',
        'Asistente',
        'Activista',
        'Maestra',
        2
    );

INSERT INTO
    preguntas (
        texto,
        opcion1,
        opcion2,
        opcion3,
        opcion4,
        indice_correcto
    )
VALUES (
        '¿Quién se queda finalmente con el billete de un trillón de dólares del Sr. Burns?',
        'Lo recupera el FBI',
        'Fidel Castro',
        'Se pierde en el agua',
        'Lo roba Smithers',
        1
    );

INSERT INTO
    preguntas (
        texto,
        opcion1,
        opcion2,
        opcion3,
        opcion4,
        indice_correcto
    )
VALUES (
        '¿Cuántas veces se ha casado Krusty el payaso?',
        '15',
        '37',
        '10',
        '2',
        0
    );

INSERT INTO
    preguntas (
        texto,
        opcion1,
        opcion2,
        opcion3,
        opcion4,
        indice_correcto
    )
VALUES (
        '¿Cómo se llamaba el exitoso grupo musical del que formó parte el Director Skinner?',
        'Captain Fantasy and the Soft-Touch Feelings',
        'Los Borbotones',
        'Cypress Creek Mens Chorus',
        'Springfield Jazz Band',
        1
    );