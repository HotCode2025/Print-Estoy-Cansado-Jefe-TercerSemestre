// Tarea: El Salto del Caballo
// Grupo: Print("Estoy cansado jefe");
// Fecha: 01/06/2026

// Comentamos el codigo para poder entenderlo paso a paso. La idea es que sea lo más claro posible.
// Ejecutamos con Quokka y esperamos a que nos devuelva el resultado.

// El tamaño del tablero lo ponemos en una variable para no hardcodear
// el número 8 por todos lados por ejemplo para no ponerlo en el for de crearTablero() o en el caso base del salto().
// . Si quisiéramos probar con un tablero
// de 6x6 por ejemplo, solo cambiamos este valor.
const N = 8;

// Estos seran los 8 movimientos que puede hacer el caballo en ajedrez.
// El caballo se mueve en forma de "L": 2 casillas en una dirección y 1 en otra.
// dx representa el desplazamiento en filas y dy en columnas.

// dx Filas "--"
// dy Columnas "|"
const dx = [ 2,  1, -1, -2, -2, -1,  1,  2];
const dy = [ 1,  2,  2,  1, -1, -2, -2, -1];


// crearTablero()
// Crea el tablero como una matriz de N x N llena de -1 para indicar que el caballo no ha pasado por ninguna casilla aún.

function crearTablero() {
  const tablero = [];

  for (let i = 0; i < N; i++) {
    // Creamos cada fila como un arreglo de N elementos, todos en -1
    tablero.push(new Array(N).fill(-1));
  }

  return tablero;
}


// esValido(x, y, tablero)
// Antes de mover el caballo, hau que verificar dos cosas:
//  1) Que las casillas (x, y) estan dentro de los limites del tablero asi no nos salimos.
//  2) Que el caballo no haya pasado antes por esa casilla (tablero[x][y] === -1)
// Si se cumplen ambas condiciones el movimiento será valido.

function esValido(x, y, tablero) {
  return (
    x >= 0 && y >= 0 &&   // que no sea negativo (no salirse por arriba/izquierda)
    x < N  && y < N  &&   // que no supere el tamaño (no salirse por abajo/derecha)
    tablero[x][y] === -1  // que la casilla no haya sido visitada
  );
}

// salto(x, y, paso, tablero)
// Esta es la función principal del algoritmo.
//
// Parámetros:
//   x, y   -> posición actual del caballo en el tablero
//   paso   -> número de movimiento que estamos intentando hacer (empieza en 1)
//   tablero -> el estado actual del tablero con los movimientos anotados
//
// La idea es:
//   - Si ya hicimos N*N movimientos (64 en total), retornamos true porque hemos encontrado una solución completa.
//   - Si no, probamos los 8 movimientos posibles desde la posición actual.
//   - Si alguno funciona, seguimos desde ahí.
//   - Si ninguno funciona, volvemos atras, es decir borramos el último movimiento y probamos otro camino

function salto(x, y, paso, tablero) {

  // Caso base: si el número de paso llegó a N*N significa que el caballo
  // recorrió todas las casillas exactamente una vez.
  if (paso === N * N) {
    return true;
  }

  // Probamos los 8 movimientos posibles del caballo
  for (let i = 0; i < 8; i++) {

    // Calculamos la nueva posición sumando el desplazamiento al (x, y) actual
    const nx = x + dx[i];
    const ny = y + dy[i];

    // Solo intentamos movernos si la casilla es válida
    if (esValido(nx, ny, tablero)) {

      // Anotamos en el tablero que esta casilla fue visitada en el paso actual
      tablero[nx][ny] = paso;

      // Llamamos recursivamente desde la nueva posición, avanzando un paso
      if (salto(nx, ny, paso + 1, tablero)) {
        return true; // Si la recursión encontró solución, la vamos devolviendo hacia arriba
      }

      // Si llegamos acá, ese camino no llevó a ningún lado.
      // Esto es basicamente lo que se llama "backtracking": deshacemos el movimiento (borramos el paso del tablero)
      tablero[nx][ny] = -1;
    }
  }

  // Si probamos los 8 movimientos y ninguno funcionó, avisamos que no hay solución desde esta posición.
  return false;
}


// mostrarTablero(tablero)
// Imprime el tablero en consola con el orden de visita de cada casilla.
// El número que aparece en cada celda indica en qué turno pasó el caballo.
// Usamos padStart(3) para que los números queden alineados y se vea prolijo.

function mostrarTablero(tablero) {
  console.log("Tablero resuelto (número de visita en cada casilla):\n");

  for (let i = 0; i < N; i++) {
    // Mapeamos cada valor: sumamos 1 para que arranque desde 1 en lugar de 0
    const fila = tablero[i]
      .map(val => String(val + 1).padStart(3))
      .join(" ");

    console.log(fila);
  }
  console.log(); // línea en blanco al final para que se vea mejor
}


// esta funcion arranca todo. Creamos el tablero, ponemos al caballo en (0,0)
// y llamamos al algoritmo. Luego  mostramos el resultado.

function main() {
  const tablero = crearTablero();

  // El caballo arranca en la posición (0, 0) y ese es su primer movimiento (paso 0)
  tablero[0][0] = 0;

  console.log(`=== Tour del Caballo en tablero ${N}x${N} ===`);
  console.log(`Posición inicial del caballo: fila 0, columna 0\n`);

  // Guardamos el tiempo antes de empezar para saber cuánto tarda el algoritmo
  const inicio = Date.now();

  // Arrancamos el algoritmo desde (0,0), el siguiente paso a buscar es el 1
  const encontrado = salto(0, 0, 1, tablero);

  const tiempoTotal = Date.now() - inicio;

  // Mostramos resultado
  if (encontrado) {
    console.log("¡Se encontró una solución!\n");
    mostrarTablero(tablero);
    console.log(`Tiempo de ejecución: ${tiempoTotal} ms`);
  } else {
    console.log("No se encontró ninguna solución para este tablero.");
  }
}

main();
