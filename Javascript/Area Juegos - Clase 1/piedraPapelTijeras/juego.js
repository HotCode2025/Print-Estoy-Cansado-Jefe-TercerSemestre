// Consigna: crear una función para darle un número aleatorio a nuestra variable pc
function aleatorio(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function jugar(eleccionUsuario) {
  // 1 = piedra, 2 = papel, 3 = tijera
  let jugador = eleccionUsuario;
  let pc = aleatorio(1, 3);

  // Capturamos los elementos donde mostraremos las elecciones
  let textoJugador = document.getElementById("eleccion-jugador");
  let textoPC = document.getElementById("eleccion-pc");
  let textoResultado = document.getElementById("resultado-final");
  let container = document.querySelector(".game-container");

  // Traducimos los números a texto para mostrarlos en el HTML
  let opcionesTexto = {
    1: "✊ Piedra",
    2: "✋ Papel",
    3: "✌️ Tijera",
  };

  textoJugador.innerText =
    "Tu elección: " + opcionesTexto[jugador];

  textoPC.innerText =
    "Elección PC: " + opcionesTexto[pc];

  // Combate y actualización del resultado
  let estado = "";
  let mensaje = "";

  if (jugador === pc) {
    estado = "empate";
    mensaje = "¡EMPATE! 🤝";
  } else if ((jugador - pc + 3) % 3 === 1) {
    estado = "ganaste";
    mensaje = "¡GANASTE! 🎉";
  } else {
    estado = "perdiste";
    mensaje = "PERDISTE ❌";
  }

  textoResultado.innerText = mensaje;
  textoResultado.className = estado;

  // Cambiamos clase CSS del contenedor
  container.className = "game-container " + estado;
}

function reiniciarJuego() {
  // Limpiamos la pantalla
  document.getElementById("eleccion-jugador").innerText =
    "Tu elección: -";

  document.getElementById("eleccion-pc").innerText =
    "Elección PC: -";

  let textoResultado =
    document.getElementById("resultado-final");

  textoResultado.innerText =
    "¡Elige una opción para empezar!";

  textoResultado.className = "";

  // Reiniciamos las clases visuales del contenedor
  document.querySelector(".game-container").className =
    "game-container";
}

// Al cargar completamente el DOM, configuramos los event listeners
document.addEventListener("DOMContentLoaded", function () {
  const botonesOpciones =
    document.querySelectorAll(".btn-opcion");

  // Le asignamos el evento click a cada botón de manera dinámica
  botonesOpciones.forEach((boton) => {
    boton.addEventListener("click", function () {
      // Obtenemos la eleccion desde el atributo data-eleccion del HTML
      let eleccion = Number(
        this.getAttribute("data-eleccion")
      );

      jugar(eleccion);
    });
  });

  // Agregamos funcionalidad al boton de reinicio
  document
    .getElementById("btn-reiniciar")
    .addEventListener("click", reiniciarJuego);
});