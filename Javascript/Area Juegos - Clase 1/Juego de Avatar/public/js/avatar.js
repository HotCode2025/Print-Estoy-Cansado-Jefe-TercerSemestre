// Variables globales
let ataqueJugador
let ataqueEnemigo

// Selección de personajes
let inputZuko = document.getElementById("Zuko")
let inputAang = document.getElementById("Aang")
let inputKatara = document.getElementById("Katara")
let inputToph = document.getElementById("Toph")

// Iniciar juego
function iniciarJuego() {
    let botonPersonajeJugador = document.getElementById("boton-personaje")
    botonPersonajeJugador.addEventListener("click", seleccionarPersonajeJugador)

    iniciarCombate()
}

// Selección del personaje del jugador
function seleccionarPersonajeJugador() {
    let spanPersonajeJugador = document.getElementById("personaje-jugador")

    if (inputZuko.checked) {
        spanPersonajeJugador.innerHTML = "Zuko"
    }
    else if (inputAang.checked) {
        spanPersonajeJugador.innerHTML = "Aang"
    }
    else if (inputKatara.checked) {
        spanPersonajeJugador.innerHTML = "Katara"
    }
    else if (inputToph.checked) {
        spanPersonajeJugador.innerHTML = "Toph"
    }
    else {
        alert("No seleccionaste ningún personaje")
        return
    }

    seleccionarPersonajeEnemigo()
}

// Selección aleatoria del enemigo
function seleccionarPersonajeEnemigo() {
    let personajeAleatorio = aleatorio(1, 4)
    let spanPersonajeEnemigo = document.getElementById("personaje-enemigo")

    switch (personajeAleatorio) {
        case 1:
            spanPersonajeEnemigo.innerHTML = "Zuko"
            break
        case 2:
            spanPersonajeEnemigo.innerHTML = "Aang"
            break
        case 3:
            spanPersonajeEnemigo.innerHTML = "Katara"
            break
        case 4:
            spanPersonajeEnemigo.innerHTML = "Toph"
            break
    }
}

// Iniciar combate
function iniciarCombate() {
    let botonPunetazo = document.getElementById("boton-punetazo")
    botonPunetazo.addEventListener("click", ataquePunetazo)

    let botonPatada = document.getElementById("boton-patada")
    botonPatada.addEventListener("click", ataquePatada)

    let botonBarrida = document.getElementById("boton-barrida")
    botonBarrida.addEventListener("click", ataqueBarrida)
}

// Ataques del jugador
function ataquePunetazo() {
    ataqueJugador = "Puñetazo"
    ataqueAleatorioEnemigo()
}

function ataquePatada() {
    ataqueJugador = "Patada"
    ataqueAleatorioEnemigo()
}

function ataqueBarrida() {
    ataqueJugador = "Barrida"
    ataqueAleatorioEnemigo()
}

// Ataque aleatorio enemigo
function ataqueAleatorioEnemigo() {
    let ataqueAleatorio = aleatorio(1, 3)

    switch (ataqueAleatorio) {
        case 1:
            ataqueEnemigo = "Puñetazo"
            break
        case 2:
            ataqueEnemigo = "Patada"
            break
        case 3:
            ataqueEnemigo = "Barrida"
            break
    }

    combate()
}

// Lógica del combate
function combate() {
    if (ataqueJugador === ataqueEnemigo) {
        crearMensaje("EMPATE")
    }
    else if (
        (ataqueJugador === "Puñetazo" && ataqueEnemigo === "Barrida") ||
        (ataqueJugador === "Patada" && ataqueEnemigo === "Puñetazo") ||
        (ataqueJugador === "Barrida" && ataqueEnemigo === "Patada")
    ) {
        crearMensaje("GANASTE")
    }
    else {
        crearMensaje("PERDISTE")
    }
}

// Crear mensaje
function crearMensaje(resultado) {
    let seccionMensaje = document.getElementById("mensajes")
    let parrafo = document.createElement("p")

    parrafo.innerHTML =
        "Tu personaje atacó con " +
        ataqueJugador +
        ", el personaje enemigo atacó con " +
        ataqueEnemigo +
        " - " +
        resultado

    seccionMensaje.appendChild(parrafo)
}

// Número aleatorio
function aleatorio(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min
}

// Cargar juego
window.addEventListener("load", iniciarJuego)