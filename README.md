# Print("Estoy Cansado Jefe") 🐍☕🟨

Repositorio con todo el contenido del Tercer Semestre.

Acá fuimos subiendo, clase a clase, todo lo que practicamos en **Java**, **Python** y **JavaScript** durante el semestre. La idea de tener los tres lenguajes juntos es poder comparar cómo se ve el mismo concepto de POO (herencia, polimorfismo, clases abstractas, etc.) en cada uno, en vez de aprenderlos como cosas separadas.

## Grupo — Print("Estoy Cansado Jefe")

- Albornoz Gian Franco
- Arreceygor Fabio
- Bruna Roy
- Cisterna Abril
- Fernández Franco
- Fernández Valentín
- Platero Martín
- Ponzina Lautaro
- Nicolás Veloz
- Sat Emir

---

Este repo agrupa **todas las clases y ejercicios del cuatrimestre**, organizados por lenguaje y por número de clase, en el mismo orden en que se fueron dando en los videos. La numeración de cada archivo (ej. `1.1`, `5.3`, `8.2`) coincide con el segmento del video correspondiente, así que se puede seguir el código en paralelo con la clase grabada.

**Qué se puede revisar por sección:**

- **Java** → desde herencia básica (Clase 1) hasta un proyecto integrador de consola con UML (Clase 10).
- **Python** → desde manejo de excepciones y archivos hasta conexión real a PostgreSQL con `psycopg2`, patrón DAO, logging y pool de conexiones.
- **JavaScript** → desde POO y modo estricto hasta los juegos del área de práctica (Torres de Hanoi, N Reinas, Piedra Papel o Tijera, Salto del Caballo y un juego de combate propio, "Juego de Avatar").

Cada carpeta de clase tiene los ejercicios resueltos en el orden en que se fueron pidiendo, y algunas (como Python Clase 7 y el Juego de Avatar) incluyen además su propio mini-README con el detalle de la consigna y el proceso de desarrollo.

Para correr los ejercicios de base de datos (Python, Clases 4 a 9) hace falta una base PostgreSQL propia y un archivo `.env` — la sección [Configuración de la base de datos](#-configuración-de-la-base-de-datos-python) explica qué variables completar.

---

.
├── Java/
│   ├── Clase 1/   → Clases padre/hija: DispositivoEntrada, Teclado, Raton, Monitor, Computadora
│   ├── Clase 2/   → Varargs, enum, bloques de inicialización
│   ├── Clase 3/   → forEach, autoboxing/unboxing, modificadores de acceso
│   ├── Clase 4/   → Overriding y polimorfismo
│   ├── Clase 5/   → Casting, clase Object, hashCode/equals, clases abstractas
│   ├── Clase 7/   → Interfaces
│   ├── Clase 8/   → JavaBeans + excepciones (incluidas las propias)
│   ├── Clase 9/   → App de consola: menú, switch, try/catch
│   └── Clase 10/  → Proyecto final: UML + app "Listar Personas"
│
├── Python/
│   ├── Clase 1/   → Excepciones (try/except, clases custom)
│   ├── Clase 2/   → Archivos: lectura, escritura, with
│   ├── Clase 3/   → Laboratorio: catálogo de películas
│   ├── Clase 4/   → Primera conexión a la base, fetchall()
│   ├── Clase 5/   → psycopg2 a fondo: fetchone, insert, update, delete
│   ├── Clase 6/   → Transacciones (manual y con with)
│   ├── Clase 7/   → UML + patrón DAO + logging
│   ├── Clase 8/   → persona_dao.py
│   └── Clase 9/   → Pool de conexiones
│
├── Javascript/
│   ├── Clase 1/   → POO base (MundoPC.js)
│   ├── Clase 2/   → Modo estricto + POO
│   ├── Clase 3/   → instanceof, polimorfismo
│   ├── Clase 4/   → try/catch/finally, throw
│   ├── Clase 5/   → Funciones flecha
│   ├── Clase 6/   → Callbacks, setTimeout/setInterval + Reloj en vivo
│   ├── Practica JS/ → Formulario de login (Web Viva)
│   └── Area Juegos - Clase 1/
│       ├── NReinas/
│       ├── Salto del Caballo/
│       ├── Torres de Hanoi/
│       ├── piedraPapelTijeras/
│       └── Juego de Avatar/   → nuestro propio juego, inspirado en Avatar: La Leyenda de Aang
│
└── README.md

> 💡 Si no nos acordamos en qué clase vimos algo, buscar por el número del archivo — están numerados igual que los segmentos del video.

### Java en una pasada

1. Clase 1 — armamos la jerarquía desde cero (padre `DispositivoEntrada` → hijas `Teclado`, `Raton`, `Monitor`, `Computadora`).
2. Clase 2 — varargs y enum.
3. Clase 3 — modificadores de acceso (`public`, `protected`, `default`).
4. Clase 4 — overriding y polimorfismo.
5. Clase 5 — casting, `Object`, `hashCode`/`equals`, clases abstractas.
6. Clase 7 — interfaces.
7. Clase 8 — JavaBeans + sistema de excepciones (propias incluidas).
8. Clase 9 — app de consola con menú y try/catch.
9. Clase 10 — entrega final: UML + app completa "Listar Personas".

### Python en una pasada

1. Clase 1 — excepciones.
2. Clase 2 — archivos.
3. Clase 3 — laboratorio de catálogo de películas.
4. Clase 4 — primera conexión a PostgreSQL.
5. Clase 5 — psycopg2 (fetch, insert, update, delete).
6. Clase 6 — transacciones.
7. Clase 7 — UML, DAO, logging.
8. Clase 8 — DAO (continuación).
9. Clase 9 — pool de conexiones.

### JavaScript en una pasada

1. Clase 1 — POO base.
2. Clase 2 — modo estricto.
3. Clase 3 — instanceof, polimorfismo.
4. Clase 4 — try/catch/finally, throw.
5. Clase 5 — funciones flecha.
6. Clase 6 — callbacks y timers + Reloj en vivo.
7. Práctica JS — login form.
8. Área de juegos — todos los proyectos jugables (ver abajo).

### Los juegos 🎮

Lo más entretenido del cuatri quedó acá:

- **N Reinas** — backtracking clásico.
- **Salto del Caballo** — recorrido completo del tablero.
- **Torres de Hanoi** — resuelve y registra cada movimiento.
- **Piedra, Papel o Tijera** — versión clásica contra la compu.
- **Juego de Avatar** — el que hicimos nosotros: elegís entre Zuko, Aang, Katara o Toph y peleás contra un enemigo aleatorio con un sistema de ataques tipo piedra/papel/tijera (Puñetazo, Patada, Barrida).

---

## ⚙️ Requisitos

- **Java**: JDK 8+. Los `.uxf` se abren con [UMLet](https://www.umlet.com/).
- **Python**: Python 3.x + `psycopg2` (`pip install psycopg2-binary`).
- **JavaScript**: cualquier navegador, no hace falta instalar nada.
- **PostgreSQL**: para correr las clases de Python con base de datos (4 a 9).

## 🔧 Configuración de la base de datos (Python)

Las clases de Python que usan PostgreSQL necesitan un archivo `.env` con estas variables:

DATABASE=
USERNAME=
PASSWORD=
HOST=
DB_PORT=

⚠️ Completar con los datos de la base local de cada uno — **no subir el `.env` con credenciales reales al repo**.

---

Cualquier duda sobre algún archivo en particular, mejor preguntar en el grupo antes de tocar el código de otro 🙏
