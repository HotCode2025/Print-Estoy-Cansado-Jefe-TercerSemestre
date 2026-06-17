import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ListadoPersona {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //Definimos la lista fuera del ciclo while
        List<Persona> personas = new ArrayList<>();
        //Empezamos con el menú
        var salir = false;
        while(!salir){
            mostrarMenu();
        }//Fin del ciclo While
    }//Fin método main


}