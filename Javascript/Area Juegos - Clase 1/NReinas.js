function NReinas(n) {
  const tablero = Array(n).fill().map(() => Array(n).fill('.'));
  const soluciones = [];

  function esValido(fila, columna) {
    // Verificar la columna
    for (let i = 0; i < fila; i++) {
      if (tablero[i][columna] === 'R') return false;
    }
    // Verificar diagonal izquierda
    for (let i = fila - 1, j = columna - 1; i >= 0 && j >= 0; i--, j--) {
      if (tablero[i][j] === 'R') return false;
    }
    // Verificar diagonal derecha
    for (let i = fila - 1, j = columna + 1; i >= 0 && j < n; i--, j++) {
      if (tablero[i][j] === 'R') return false;
    }
    return true;
  }

  function retroceder(fila) {
    if (fila === n) {
      soluciones.push(tablero.map(r => r.join('')));
      return;
    }
    for (let columna = 0; columna < n; columna++) {
      if (esValido(fila, columna)) {
        tablero[fila][columna] = 'R';
        retroceder(fila + 1);
        tablero[fila][columna] = '.';
      }
    }
  }

  retroceder(0);

  // Mostrar soluciones en consola
  soluciones.forEach((solucion, i) => {
    console.log(`Solución ${i + 1}:`);
    solucion.forEach(fila => console.log(fila));
    console.log("\n");
  });
}

// Ejemplo: n = 4
NReinas(8);
