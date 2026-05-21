let inputZuko = document.getElementById("Zuko")
let inputAang = document.getElementById("Aang")
let inputKatara = document.getElementById("Katara")
let inputToph = document.getElementById("Toph")

function seleccionarPersonajeJugador() {

    if (inputZuko.checked) {
        alert("Elegiste a Zuko")
    } 
    
    else if (inputAang.checked) {
        alert("Elegiste a Aang")
    } 
    
    else if (inputKatara.checked) {
        alert("Elegiste a Katara")
    } 
    
    else if (inputToph.checked) {
        alert("Elegiste a Toph")
    } 
    
    else {
        alert("No seleccionaste ningún personaje")
    }
}

let botonPersonajeJugador = document.getElementById("boton-personaje")

botonPersonajeJugador.addEventListener("click", seleccionarPersonajeJugador)