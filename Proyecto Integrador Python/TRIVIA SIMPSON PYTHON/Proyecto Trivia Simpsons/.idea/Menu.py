import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPresiona ENTER para continuar...")

def jugar():
    limpiar_pantalla()
    print("=== COMIENZA EL JUEGO ===")
    nombre = input("Ingresa tu nombre de jugador: ").strip()
    while not nombre:
        nombre = input("El nombre no puede estar vacío. Inténtalo de nuevo: ").strip()
    print(f"\n¡Preparado {nombre}! Iniciando partida...")
    pausar()

def mostrar_reglas():
    limpiar_pantalla()
    print("==================================================")
    print("               REGLAS DEL JUEGO                   ")
    print("==================================================")
    print("1. El juego consta de preguntas de opción múltiple.")
    print("2. Cada respuesta correcta sumará puntos a tu puntaje.")
    print("3. Las respuestas incorrectas no restan, pero pierdes la racha.")
    print("4. Tienes un límite de tiempo por pregunta (si aplica).")
    print("5. No se permiten espacios vacíos en el nombre del jugador.")
    print("6. Al finalizar, tu puntaje se guardará en el ranking global.")
    print("7. ¡Evita el 'D´oh!' de Homero y demuestra cuánto sabes!")
    print("==================================================")
    pausar()

class Puntuacion:
    @staticmethod
    def mostrar_puntajes():
        limpiar_pantalla()
        print("==================================================")
        print("               RANKING GLOBAL                     ")
        print("==================================================")
        print("[Conectando con la base de datos...]")
        print("[Cargando tabla de posiciones desde la BD...]")
        print("==================================================")

def iniciar_juego():
    while True:
        limpiar_pantalla()
        print("==============================")
        print("         PYTHON D´OH!         ")
        print("==============================")
        print("1. JUGAR")
        print("2. REGLAS")
        print("3. PUNTAJES")
        print("4. SALIR")
        print("==============================")

        opcion = input("Ingrese una opcion (1 al 4): ").strip()

        match opcion:
            case "1":
                jugar()
            case "2":
                mostrar_reglas()
            case "3":
                Puntuacion.mostrar_puntajes()
                pausar()
            case "4":
                limpiarpantalla()
                print("Saliendo del programa... ¡Adiós, caramba!")
                break
            case :
                print("Opción no válida. Por favor, ingrese un número del 1 al 4.")
                pausar()

if name == "main":
    iniciar_juego()