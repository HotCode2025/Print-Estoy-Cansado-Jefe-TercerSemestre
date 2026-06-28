document.addEventListener("DOMContentLoaded", () => {
    // Cantidad de nubes
    const numNubes = 20;
    
    for (let i = 0; i < numNubes; i++) {
        let nube = document.createElement("div");
        nube.className = "nube";
        
        // posicion vertical aleatoria
        nube.style.top = Math.random() * 50 + "vh";
        nube.style.left = Math.random() * 20 + "vw";
        
        // tamaño aleatorio mas o menos
        let scale = Math.random() * 3.8 + 1.4; // nubes grandes y pequeñas
        nube.style.opacity = Math.random() * 0.4 + 0.4; // transparencia aleatoria
        
        // velocidad
        let duracion = Math.random() * 20 + 20; // entre 20 y 40 seg.
        nube.style.animationDuration = duracion + "s";
        
        // desfase; para que no salgan todas juntas
        nube.style.animationDelay = (Math.random() * -40) + "s";
        
        // aplicar la escala usando una variable CSS personalizada
        nube.style.setProperty('--scale', scale);
        
        document.body.appendChild(nube);
    }
});
