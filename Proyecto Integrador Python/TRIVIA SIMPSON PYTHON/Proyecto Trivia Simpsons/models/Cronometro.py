import time

def formatear(segundos):
    minutos = int(segundos // 60)
    segs = segundos % 60
    return f"{minutos:02d}:{segs:05.2f}"

LIMITE = 150  # 2 minutos y 30 segundos

class Cronometro:
    def __init__(self):
        self.inicio = None
        self.corriendo = False

    def iniciar(self):
        self.inicio = time.time()
        self.corriendo = True

    def detener(self):
        if self.corriendo:
            self.corriendo = False
            return self.tiempo_actual()
        return 0

    def tiempo_actual(self):
        if self.corriendo:
            return time.time() - self.inicio
        return 0

    def tiempo_restante(self):
        return max(0, LIMITE - self.tiempo_actual())

    def se_acabo(self):
        return self.tiempo_actual() >= LIMITE

    def mostrar(self):
        while self.corriendo:
            actual = self.tiempo_actual()

            if actual >= LIMITE:
                print(f"\nTiempo limite alcanzado! {formatear(LIMITE)}")
                self.corriendo = False
                break

            restante = LIMITE - actual
            if restante <= 30:
                print(f"\r{formatear(actual)}  Quedan {int(restante)}s ", end="", flush=True)
            else:
                print(f"\r{formatear(actual)}", end="", flush=True)

            time.sleep(0.01)