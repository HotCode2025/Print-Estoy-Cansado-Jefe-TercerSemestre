USE simpsons_trivia;

-- Insertar preguntas de ejemplo --
INSERT INTO preguntas (texto, indice_correcto) VALUES
('¿Cuántos miembros tiene la familia Simpson de forma principal?', 0),
('¿Cómo se llama el dueño del minisuper (Kwik-E-Mart)?', 1);

-- Insertar opciones/respuestas (asociadas por id de pregunta)
INSERT INTO respuestas (pregunta_id, texto, es_correcta) VALUES
(1, '5', TRUE), (1, '4', FALSE), (1, '7', FALSE),
(2, 'Homero', FALSE), (2, 'Apu', TRUE), (2, 'Ned', FALSE);