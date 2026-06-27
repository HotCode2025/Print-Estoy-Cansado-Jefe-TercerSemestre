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
    nombre_jugador TEXT NOT NULL,
    puntaje INTEGER NOT NULL DEFAULT 0,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Insertamos las preguntas iniciales directamente en la base de datos
INSERT INTO preguntas (texto, opcion1, opcion2, opcion3, opcion4, indice_correcto)
VALUES ('¿Cuántos integrantes tiene la familia Simpson?', '3', '4', '5', '6', 2);

INSERT INTO preguntas (texto, opcion1, opcion2, opcion3, opcion4, indice_correcto)
VALUES ('¿Cómo se llama el jefe de Homero?', 'Ned Flanders', 'Montgomery Burns', 'Moe Szyslak', 'Waylon Smithers', 2);

-- Datos de prueba para el ranking
INSERT INTO ranking (nombre_jugador, puntaje) VALUES ('Bart', 10);
INSERT INTO ranking (nombre_jugador, puntaje) VALUES ('Lisa', 100);
INSERT INTO ranking (nombre_jugador, puntaje) VALUES ('Milhouse', 5);