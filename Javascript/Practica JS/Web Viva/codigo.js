document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.querySelector("form");
    const mensajeError = document.getElementById("mensaje-error");

    loginForm.addEventListener("submit", function(event) {
        event.preventDefault();
        
        const inputs = loginForm.querySelectorAll("input");
        const usuario = inputs[0].value;
        const password = inputs[1].value;

        if (usuario === "admin" && password === "1234") {
            window.location.href = "exito.html";
        } else {
            // Ahora sí reconocerá la variable
            mensajeError.classList.remove("hidden");
            
            setTimeout(() => {
                mensajeError.classList.add("hidden");
            }, 3000);
        }
    });
});