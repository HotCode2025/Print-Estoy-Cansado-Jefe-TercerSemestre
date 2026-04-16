package org.example;

public class Resolución_tarea_CLASE_2 {
  //  El bloque estático "static" se usa para configurar variables de clase

  //  Una posible solución para reemplazarlo sería (si la lógica es simple) inicializando la variable en su propia declaración, si por el contrario es mas compleja, usando un método estático privado.

    //        - Inicialización Directa con Métodos Privados

    public class Persona {
        private final int idPersona;
        // REEMPLAZO STATIC: Inicialización directa
        private static int contadorPersonas = 0;

        public Persona() {
            // REEMPLAZO NO ESTÁTICO: Lógica movida al constructor
            this.idPersona = asignarId();
            System.out.println("Ejecución del constructor");
        }

        // Método privado para encapsular la lógica que antes estaba "suelta"
        private int asignarId() {
            System.out.println("Ejecución de la lógica de instancia");
            return ++Persona.contadorPersonas;
        }

        public int getIdPersona() {
            return this.idPersona;
        }

        @Override
        public String toString() {
            return "Persona{idPersona=" + idPersona + "}";
        }
    }

}
