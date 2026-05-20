function resolver() {
  const n = parseInt(document.getElementById("valorN").value);
  const contenedor = document.getElementById("soluciones");
  
  contenedor.innerHTML = "";

  if (isNaN(n) || n < 4 || n > 13) {
    contenedor.innerHTML = "<p style='color: #dc2626; font-weight: bold; font-size: 1.2em; background-color: #fee2e2; padding: 15px; border-radius: 8px; border: 2px solid #fca5a5;'>⚠️ Error: Por favor, introduce un número entre 4 y 13.</p>";
    return;
  }

  const resultados = [];
  const tablero = Array(n).fill().map(() => Array(n).fill('.'));

  function esValido(fila, col) {
    for (let i = 0; i < fila; i++) {
      if (tablero[i][col] === 'Q') return false;
    }
    for (let i = fila - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
      if (tablero[i][j] === 'Q') return false;
    }
    for (let i = fila - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
      if (tablero[i][j] === 'Q') return false;
    }
    return true;
  }

  function backtrack(fila) {
    if (fila === n) {
      resultados.push(tablero.map(r => r.join('')));
      return;
    }
    for (let col = 0; col < n; col++) {
      if (esValido(fila, col)) {
        tablero[fila][col] = 'Q';
        backtrack(fila + 1);
        tablero[fila][col] = '.';
      }
    }
  }

  backtrack(0);

  let solucionesAMostrar = resultados;
  if (resultados.length > 4) {
    solucionesAMostrar = resultados.sort(() => 0.5 - Math.random()).slice(0, 4);
  }

  if (solucionesAMostrar.length === 0) {
    contenedor.innerHTML = "<p style='color: #1e3a8a; font-weight: bold;'>No hay soluciones para N=" + n + "</p>";
    return;
  }

  solucionesAMostrar.forEach(sol => {
    const divTablero = document.createElement("div");
    divTablero.className = "tablero";
    sol.forEach(fila => {
      const filaDiv = document.createElement("div");
      filaDiv.className = "fila";
      fila.split("").forEach(celda => {
        const celdaDiv = document.createElement("div");
        celdaDiv.className = "celda";
        if (celda === "Q") {
          celdaDiv.innerHTML = "<span class='reina'>♛</span>";
        }
        filaDiv.appendChild(celdaDiv);
      });
      divTablero.appendChild(filaDiv);
    });
    contenedor.appendChild(divTablero);
  });
}