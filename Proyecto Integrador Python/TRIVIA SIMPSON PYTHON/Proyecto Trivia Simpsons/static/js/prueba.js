document.addEventListener("DOMContentLoaded", () => {
    // rosquillas cada 600ms
    setInterval(crearRosquilla, 600);

    // musica de fondo
    const bgMusic = document.getElementById("bg-music");
    if (bgMusic) {
        bgMusic.volume = 0.04;
        let playPromise = bgMusic.play();
        if (playPromise !== undefined) {
            playPromise.catch(() => {
                // autoplay bloqueado
                const iniciarMusica = () => {
                    bgMusic.play();
                    document.removeEventListener("click", iniciarMusica);
                };
                document.addEventListener("click", iniciarMusica);
            });
        }
    }

    function crearRosquilla() {
        const rosquilla = document.createElement("div");
        rosquilla.innerText = "🍩"; 
        
        // estilo inicial
        rosquilla.style.position = "fixed";
        rosquilla.style.top = "-50px";
        rosquilla.style.left = Math.random() * 100 + "vw"; 
        rosquilla.style.fontSize = (Math.random() * 20 + 15) + "px"; 
        rosquilla.style.opacity = Math.random() * 0.5 + 0.3; 
        rosquilla.style.zIndex = "-1"; 
        rosquilla.style.transition = "top 6s linear, transform 6s linear";
        rosquilla.style.pointerEvents = "none"; 
        
        document.body.appendChild(rosquilla);

        // animacion
        setTimeout(() => {
            rosquilla.style.top = "110vh";
            rosquilla.style.transform = `rotate(${Math.random() * 360}deg)`;
        }, 50);

        // Limpiar memoria al terminar
        setTimeout(() => {
            rosquilla.remove();
        }, 6000);
    }
});
