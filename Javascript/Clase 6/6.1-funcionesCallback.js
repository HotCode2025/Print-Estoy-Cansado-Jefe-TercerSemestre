miFuncion1();
miFuncion2();

function miFuncion1() {
  console.log('Función 1');
}

function miFuncion2() {
  console.log('Función 2');
}

// Función de tipo callback
let impr = function imprimir(mensaje) {
  console.log(mensaje);
}

function sumar(op1, op2, funcionCallback) {
  let resultado = op1 + op2;
  funcionCallback(`El resultado es: ${resultado}`);
}

// Llamada con callback
sumar(5, 3, impr);
