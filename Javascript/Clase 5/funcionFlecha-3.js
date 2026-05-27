//Continuamos con otro ejemplo
const regresaObjeto = () => ({ nombre: 'Juan', apellido: 'Lara'});

console.log(regresaObjeto());

//Funciones flecha que reciben parámetros
const funcionParametros = ( mensaje ) => console. log( mensaje );

funcionParametros('saludos desde esta funcion con parametros');

//Una función clásica
const funcionParametrosClasica = function( mensaje ){
console.log( mensaje );

}

funcionParametrosClasica('Saludos desde la funcion clasica')

//Se pueden omitir los paréntesis enla función flecha de la siguiente manera
const funcionConParametros = mensaje => console.log( mensaje );

funcionConParametros('Otra forma de trabajar con funcion flecha');