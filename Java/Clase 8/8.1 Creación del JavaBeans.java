package domain;

import java.io.Serializable;
public class persona implements Serializable{
    private String nombre;
    private String apellido;

    //Constructor vacio: Esto es obligatorio
    public persona() {
    }

    public persona(String nombre, String apellido) {
        this.nombre = nombre;
        this.apellido = apellido;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    @Override
    public String toString() {
        return "persona{" + "nombre=" + nombre + ", apellido=" + apellido + '}';
    }
}
