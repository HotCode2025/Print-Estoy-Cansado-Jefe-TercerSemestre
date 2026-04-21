// Clase base para dispositivos de entrada
class DispositivoEntrada {
    constructor(tipoEntrada, marca) {
        this._tipoEntrada = tipoEntrada;
        this._marca = marca;
    }
    // Getter para tipoEntrada
    get tipoEntrada() {
        return this._tipoEntrada;
    }
    // Setter para tipoEntrada
    set tipoEntrada(tipoEntrada) {
        this._tipoEntrada = tipoEntrada;
    }
    // Getter para marca
    get marca() {
        return this._marca;
    }
    // Setter para marca
    set marca(marca) {
        this._marca = marca;
    }
}

// Clase para ratón, hereda de DispositivoEntrada
class Raton extends DispositivoEntrada {
    static contadorRatones = 0;

    constructor(tipoEntrada, marca) {
        super(tipoEntrada, marca);
        this._idRaton = ++Raton.contadorRatones;
    }
    // Getter para idRaton
    get idRaton() {
        return this._idRaton;
    }
    // Método toString para representar el objeto
    toString() {
        return `Raton: [idRaton: ${this._idRaton}, tipoEntrada: ${this.tipoEntrada}, marca: ${this.marca}]`;
    }
}

// Creación de instancias de ratón
let raton1 = new Raton('USB', 'HP');
console.log(raton1.toString());
let raton2 = new Raton('Bluetooth', 'Logitech');
console.log(raton2.toString());

// Clase para teclado, hereda de DispositivoEntrada
class Teclado extends DispositivoEntrada {
    static contadorTeclados = 0;

    constructor(tipoEntrada, marca) {
        super(tipoEntrada, marca);
        this._idTeclado = ++Teclado.contadorTeclados;
    }
    // Getter para idTeclado
    get idTeclado() {
        return this._idTeclado;
    }
    toString() {
        return `Teclado: [idTeclado: ${this._idTeclado}, tipoEntrada: ${this.tipoEntrada}, marca: ${this.marca}]`;
    }
}

// Creación de instancias de teclado
let teclado1 = new Teclado('USB', 'Redragon');
console.log(teclado1.toString());
let teclado2 = new Teclado('Bluetooth', 'Asus');
console.log(teclado2.toString());

// Clase para monitor
class Monitor {
    static contadorMonitores = 0;

    constructor (marca, tamanio){
        this._idMonitor = ++Monitor.contadorMonitores;
        this._marca = marca;
        this._tamanio = tamanio;
    }
    // Getter para idMonitor
    get idMonitor(){
        return this._idMonitor;
    }
    // Método toString para representar el objeto
    toString(){
        return `Monitor: [idMonitor: ${this._idMonitor}, marca: ${this._marca}, tamaño: ${this._tamanio}]`;
    }
    
}
// Creación de instancias de monitor
let monitor1 = new Monitor('HP', 15);
let monitor2 = new Monitor('Dell', 27);
console.log(monitor1.toString())
console.log(monitor2.toString())

// Clase para computadora, que agrupa monitor, ratón y teclado
class Computadora {
    static contadorComputadoras = 0;
    constructor(nombre, monitor, raton, teclado){
        this._idComputadora = ++Computadora.contadorComputadoras;
        this._nombre = nombre;
        this._monitor = monitor;
        this._raton = raton;
        this._teclado = teclado;
    }
    // Método toString para representar la computadora y sus componentes
    toString(){
    return `Computadora ${this._idComputadora}: ${this._nombre}\n ${this._monitor}\n  ${this._raton}\n ${this._teclado}`;
    }
}

// Creación de instancias de computadora
let computadora1 = new Computadora('HP', monitor1, raton1, teclado1);
console.log(computadora1.toString());
console.log(`${computadora1}`);
let computadora2 = new Computadora('Aser', monitor2, raton2, teclado2);
console.log(`${computadora2}`);

class Orden {
    static contadorOrdenes = 0;

    constructor() {
        this._idOrden = ++Orden.contadorOrdenes;
        this._computadoras = [];
    }
    get idOrden(){
        return this._idOrden;
    }
    agregarComputadora(computadora){
        this._computadoras.push(computadora);
    }
    mostrarOrden(){
        let computadorasOrden = '';
        for( let computadora of this._computadoras){
            computadorasOrden+= `\n${computadora}`;
        }
        console.log(`Orden: ${this._idOrden}, Computadoras: ${computadorasOrden}`);
    }
}

let orden1 = new Orden();
orden1.agregarComputadora(computadora1);
orden1.agregarComputadora(computadora2);
orden1.agregarComputadora(computadora2);//Se puede repetir una orden
orden1.mostrarOrden();

let orden2 = new Orden();
orden2.agregarComputadora(computadora2);
orden2.agregarComputadora(computadora1);
orden2.mostrarOrden();

// CLASE 3 JAVASCRIPT POLIMORFISMO 20/04/2026
// GRUPO PRINT("ESTOY CANSADO JEFE");

// Primero vamos a definir una funcion polimorfica

// Explicado sencillamente, esta función es polimórfica porque puede trabajar con objetos de diferentes clases 
// (Raton, Monitor, Teclado) sin necesidad de conocer su tipo específico. 
// Esto permite que la función sea flexible y reutilizable para cualquier dispositivo que implemente el método toString().

function probarDispositivo(dispositivo) {
    // Esta función no necesita evaluar si el "dispositivo" es un Raton o un Monitor.
    // Solo confía en la interfaz común; delega la responsabilidad de la representación al objeto.
    console.log(dispositivo.toString());
}

// Al ejecutar la función, cada objeto va a responder con su propia implementación
probarDispositivo(raton1);
probarDispositivo(monitor1);