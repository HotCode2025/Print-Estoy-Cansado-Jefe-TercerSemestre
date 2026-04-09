// 1.6 Comenzamos las pruebas creando objetos de cada clase y las agregamos a la lista de Orden
package ar.com.system2023.mundpc.mundopc;
import ar.com.system2023.mundopc.*;

public class MundoPc {
    public static void main(String[] args) {
        // Video 8
        Monitor monitorHP = new Monitor("HP", 23); // Importamos la clase
        Teclado tecladoHP = new Teclado("Bluetooth", "HP");
        Raton ratonHP = new Raton("Bluetooth", "HP");
        Computadora compuHP = new Computadora("Computadora HP", monitorHP, tecladoHP, ratonHP);

        // Creamos otro objeto de distinta marca
        Monitor monitorGamer = new Monitor("Gamer", 32);
        Teclado tecladoGamer = new Teclado("Bluetooth", "Gamer");
        Raton ratonGamer = new Raton("Bluetooth", "Gamer");
        Computadora compuGamer = new Computadora("Computadora Gamer", monitorGamer, tecladoGamer, ratonGamer);

        // Dell
        Monitor monitorDell = new Monitor("Dell", 27);
        Teclado tecladoDell = new Teclado("USB", "Dell");
        Raton ratonDell = new Raton("USB", "Dell");
        Computadora compuDell = new Computadora("Computadora Dell", monitorDell, tecladoDell, ratonDell);

        // Lenovo
        Monitor monitorLenovo = new Monitor("Lenovo", 24);
        Teclado tecladoLenovo = new Teclado("Inalámbrico", "Lenovo");
        Raton ratonLenovo = new Raton("Inalámbrico", "Lenovo");
        Computadora compuLenovo = new Computadora("Computadora Lenovo", monitorLenovo, tecladoLenovo, ratonLenovo);

        // Apple
        Monitor monitorApple = new Monitor("Apple", 29);
        Teclado tecladoApple = new Teclado("Bluetooth", "Apple");
        Raton ratonApple = new Raton("Bluetooth", "Apple");
        Computadora compuApple = new Computadora("Computadora Apple", monitorApple, tecladoApple, ratonApple);

        // Asus
        Monitor monitorAsus = new Monitor("Asus", 31);
        Teclado tecladoAsus = new Teclado("USB", "Asus");
        Raton ratonAsus = new Raton("USB", "Asus");
        Computadora compuAsus = new Computadora("Computadora Asus", monitorAsus, tecladoAsus, ratonAsus);

        // Acer
        Monitor monitorAcer = new Monitor("Acer", 21);
        Teclado tecladoAcer = new Teclado("Inalámbrico", "Acer");
        Raton ratonAcer = new Raton("Inalámbrico", "Acer");
        Computadora compuAcer = new Computadora("Computadora Acer", monitorAcer, tecladoAcer, ratonAcer);

        // MSI
        Monitor monitorMSI = new Monitor("MSI", 34);
        Teclado tecladoMSI = new Teclado("USB", "MSI");
        Raton ratonMSI = new Raton("USB", "MSI");
        Computadora compuMSI = new Computadora("Computadora MSI", monitorMSI, tecladoMSI, ratonMSI);

        // Razer
        Monitor monitorRazer = new Monitor("Razer", 27);
        Teclado tecladoRazer = new Teclado("Inalámbrico", "Razer");
        Raton ratonRazer = new Raton("Inalámbrico", "Razer");
        Computadora compuRazer = new Computadora("Computadora Razer", monitorRazer, tecladoRazer, ratonRazer);

        // Samsung
        Monitor monitorSamsung = new Monitor("Samsung", 28);
        Teclado tecladoSamsung = new Teclado("Bluetooth", "Samsung");
        Raton ratonSamsung = new Raton("Bluetooth", "Samsung");
        Computadora compuSamsung = new Computadora("Computadora Samsung", monitorSamsung, tecladoSamsung, ratonSamsung);

        // Video 9
        Orden orden1 = new Orden(); // Inicializamos un arreglo vacio
        Orden orden2 = new Orden(); // Nueva lista para el objeto orden2
        //Orden 1 llega a 10 elementos
        orden1.agregarComputadora(compuHP);
        orden1.agregarComputadora(compuGamer);
        orden1.agregarComputadora(compuDell);
        orden1.agregarComputadora(compuLenovo);
        orden1.agregarComputadora(compuApple);
        orden1.agregarComputadora(compuAsus);
        orden1.agregarComputadora(compuAcer);
        orden1.agregarComputadora(compuMSI);
        orden1.agregarComputadora(compuRazer);
        orden1.agregarComputadora(compuSamsung);


        // Video 10
        Computadora compusVarias = new Computadora("Computadora de diferentes marcas", monitorHP, tecladoGamer, ratonHP);
        orden2.agregarComputadora(compusVarias);
        System.out.println("Orden 1: ");
        orden1.mostrarOrden();
        System.out.println("\nOrden 2: ");
        orden2.mostrarOrden();
    }
}
