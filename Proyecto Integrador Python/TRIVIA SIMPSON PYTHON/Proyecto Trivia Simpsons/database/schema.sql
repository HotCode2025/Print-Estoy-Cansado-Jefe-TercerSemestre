DROP TABLE IF EXISTS opciones;
DROP TABLE IF EXISTS preguntas;
DROP TABLE IF EXISTS ranking;

CREATE TABLE ranking (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_jugador TEXT NOT NULL,
    puntaje INTEGER NOT NULL DEFAULT 0,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Datos de prueba para el ranking
INSERT INTO ranking (nombre_jugador, puntaje) VALUES ('Bart', 10);
INSERT INTO ranking (nombre_jugador, puntaje) VALUES ('Lisa', 100);
INSERT INTO ranking (nombre_jugador, puntaje) VALUES ('Milhouse', 5);