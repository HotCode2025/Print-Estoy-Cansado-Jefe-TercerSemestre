
mifuncion1();
mifuncion2();


function mifuncion1() {
    console.log('Función 1');
}

function mifuncion2() {
    console.log('Función 2');
}

//Función de tipo callback
let imp = function imprimir(mensaje) {
    console.log(mensaje); 
}

function sumar(op1, op2, funcionCallback) {
    let res = op1 + op2;
    funcionCallback(`Resultado: ${res}`);
}

sumar(5, 3, imp);

//llamdas asincronas con uso de setTimeout
function miFuncionCallback() {
    console.log('Saludo asincrono después de 3 segundos');
}

setTimeout(miFuncionCallback, 5000);

setTimeout(function() { console.log('Saludo asincrono 2'); }, 3000);

setTimeout(() => console.log('Saludos Asincrono 3'), 4000);
