package test;

import domain.Persona;

public class TestBloqueInicializacion {
    public static void main(String[] args) {
        Persona persona1 = new Persona();

        // Mostramos el estado final tras inicializar
        System.out.println("persona1 = " + persona1);
    }
}