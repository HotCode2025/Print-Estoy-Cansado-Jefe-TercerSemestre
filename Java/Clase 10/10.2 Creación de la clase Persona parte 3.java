public class Persona {
    private String nombre;
    private String tel;
    private String email;
    private static int numeroPersonas = 0;

    //Constructor vacio
    public Persona(){
        this.id = ++Persona.numeroPersonas;
    }

    //Constructor con parámetros(sobrecarga de constructores)
    public Persona(String nombre, String tel, String email){
        this();
        this.nombre = nombre;
        this.tel = tel;
        this.email = email;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public String setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getTel() {
        return tel;
    }

    public String setTel(String tel) {
        this.tel = tel;
    }
    
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

}