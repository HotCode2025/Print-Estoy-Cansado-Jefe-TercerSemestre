const fondos = [
    "https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?q=80&w=2070", // Mañana
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb?q=80&w=2070", // Paisaje
    "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?q=80&w=2044", // Ciudad Noche
    "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072", // Espacial/Tech
    "https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=2070" // Retro/Setup
    
];

let indiceFondo = 0;

document.body.style.backgroundImage = `url('${fondos[indiceFondo]}')`;

const btn = document.getElementById('btn-fondo');

btn.addEventListener('click', () => {
    indiceFondo++;
    
    // Condicional para volver al primer fondo
    if (indiceFondo >= fondos.length) {
        indiceFondo = 0;
    }
    
    document.body.style.backgroundImage = `url('${fondos[indiceFondo]}')`;
});
function actualizarReloj() {
    const ahora = new Date();
    
    // --- LÓGICA DE RELOJ ---
    let h = String(ahora.getHours()).padStart(2, '0');
    let m = String(ahora.getMinutes()).padStart(2, '0');
    let s = String(ahora.getSeconds()).padStart(2, '0');
    document.getElementById('reloj').textContent = `${h}:${m}:${s}`;

    // --- LÓGICA DE LA FECHA ---
    const opciones = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    let fechaActual = ahora.toLocaleDateString('es-ES', opciones);
    document.getElementById('fecha').textContent = fechaActual;

    // --- MODIFICADOR DE FONDOS ---
    actualizarFondo(ahora.getHours());
}



setInterval(actualizarReloj, 1000);
actualizarReloj();