# Proyecto Integrador Python - Trivia Simpsons

Probando Flask (framework de Python).

## Instalacion y Entorno Virtual

Para compartir el proyecto y que otra persona no tenga que buscar que librerias instalar, utilizamos un "entorno virtual" junto con el archivo `requirements.txt`. No se debe compartir la carpeta del entorno virtual, solo el archivo `requirements.txt`.

Sigue estos pasos para levantar el proyecto en otra computadora:

1. Abrir la terminal en la carpeta del proyecto.

2. Crear el entorno virtual:
   python -m venv .venv

3. Activar el entorno virtual:
   - En Windows:
     .venv\Scripts\activate
   - En Linux:
     source .venv/bin/activate

4. Instalar las dependencias (librerias como Flask):
   "pip install -r requirements.txt"

Una vez hecho esto, el proyecto estara listo para ejecutarse con todas las librerias necesarias.

## ¿Cómo funciona este proyecto? (Arquitectura) Ojito!!! :3

Para que todos podamos trabajar en equipo sin pisarnos, el proyecto está dividido en partes. **Python (usando Flask) es el núcleo (Backend)** que conecta todo:

1. **La Base de Datos (Memoria):** Aquí guardamos las preguntas y el ranking. Python es el único que "habla" directamente con la base de datos (para leer o guardar cosas, aclaro).

2. **El Núcleo (Python / Flask):** Recibe las peticiones del user en el archivo `App.py`. Por ejemplo, si el user hace clic en "Jugar", Python busca las preguntas en la base de datos y se las manda a la página web (O sea, se las manda al Frontend).

3. **El Frontend (HTML, CSS, JS):** Es lo que ve el user. El HTML/CSS le da la estructura y el diseño, y el JavaScript (JS) se encarga de la interactividad y de mostrar los datos que le envía Python.

**¿Cómo nos dividimos el trabajo? :3**
Con esta estructura, podemos dividirnos tareas fácilmente y que todos tengan commits en el repositorio:

- **Diseño visual:** Alguien puede encargarse de hacerlo piola a las vistas en la carpeta `templates` (HTML) y mejorar los estilos en `static/css`.
- **Interactividad Frontend:** Alguien puede programar la lógica del juego del lado del cliente usando JavaScript.
- **Base de Datos:** Alguien puede encargarse de crear la base de datos (SQLite), armar las tablas e insertar las preguntas.
- **Lógica Backend:** Alguien puede trabajar en `App.py` para crear las funciones de Python que envían y reciben la información entre la base de datos y el HTML.
