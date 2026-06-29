import time
import msvcrt

def formatear(segundos):
    minutos = int(segundos // 60)
    segs = segundos % 60
    return f"{minutos:02d}:{segs:05.2f}"

LIMITE = 180  # 3 minutos en segundos

def cronometro():
    print("=== CRONOMETRO (limite: 3 minutos) ===")
    print("Comandos: [Enter] iniciar/pausar | [v] vuelta | [r] reiniciar | [q] salir\n")

    inicio = None
    transcurrido = 0
    corriendo = False
    vueltas = []
    inicio_vuelta = None

    while True:
        if msvcrt.kbhit():
            tecla = msvcrt.getwch().lower()

            if tecla == '\r':  # Enter
                if not corriendo:
                    inicio = time.time() - transcurrido
                    inicio_vuelta = inicio_vuelta or time.time()
                    corriendo = True
                    print(" Corriendo...")
                else:
                    transcurrido = time.time() - inicio
                    corriendo = False
                    print(f" Pausado en {formatear(transcurrido)}")

            elif tecla == 'v' and corriendo:
                ahora = time.time()
                tiempo_vuelta = ahora - inicio_vuelta
                inicio_vuelta = ahora
                transcurrido_actual = ahora - inicio
                vueltas.append((len(vueltas)+1, tiempo_vuelta, transcurrido_actual))
                print(f"  Vuelta {len(vueltas)}: {formatear(tiempo_vuelta)}  |  Total: {formatear(transcurrido_actual)}")

            elif tecla == 'r':
                corriendo = False
                transcurrido = 0
                inicio_vuelta = None
                vueltas = []
                print(" Reiniciado\n")

            elif tecla == 'q':
                print("Saliendo...")
                break

        if corriendo:
            actual = time.time() - inicio

            # Chequeo del limite de 3 minutos
            if actual >= LIMITE:
                print(f"\n Tiempo limite alcanzado! {formatear(LIMITE)}")
                print(f"   Vueltas registradas: {len(vueltas)}")
                corriendo = False
                transcurrido = LIMITE
                break

            # Aviso cuando quedan 30 segundos
            restante = LIMITE - actual
            if restante <= 30:
                print(f"\r {formatear(actual)}    Quedan {int(restante)}s ", end="", flush=True)
            else:
                print(f"\r {formatear(actual)}", end="", flush=True)

            time.sleep(0.01)

cronometro()