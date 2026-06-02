const estadoInicial = [
    [5,4,3,2,1],
    [],
    []
];

let torres = JSON.parse(JSON.stringify(estadoInicial));
let origen = null;
let movimientos = 0;

const colores = [
    "#ef4444",
    "#f97316",
    "#eab308",
    "#22c55e",
    "#3b82f6"
];

const contador = document.getElementById("movimientos");

function renderizar(){

    document.querySelectorAll(".torre").forEach((torre,index)=>{

        torre.querySelectorAll(".disco").forEach(d=>d.remove());

        torres[index].forEach(tam=>{

            const disco = document.createElement("div");

            disco.classList.add("disco");

            disco.style.width = `${tam * 35 + 50}px`;
            disco.style.background = colores[tam - 1];

            torre.appendChild(disco);
        });
    });

    contador.textContent = movimientos;
}

function moverDisco(origen,destino){

    if(torres[origen].length === 0) return;

    const disco = torres[origen][torres[origen].length - 1];

    if(
        torres[destino].length === 0 ||
        disco < torres[destino][torres[destino].length - 1]
    ){

        torres[origen].pop();
        torres[destino].push(disco);

        movimientos++;

        verificarVictoria();

        renderizar();
    }
}

document.querySelectorAll(".torre").forEach(torre=>{

    torre.addEventListener("click",()=>{

        const indice = Number(torre.dataset.torre);

        if(origen === null){

            origen = indice;
            torre.style.filter = "drop-shadow(0 0 15px #38bdf8)";

        }else{

            document.querySelectorAll(".torre")
                .forEach(t=>t.style.filter="none");

            moverDisco(origen,indice);

            origen = null;
        }
    });
});

function verificarVictoria(){

    if(torres[2].length === 5){

        setTimeout(()=>{

            alert(
                `¡Felicitaciones!\n\nCompletaste el juego en ${movimientos} movimientos.`
            );

        },200);
    }
}

document.getElementById("reiniciar")
.addEventListener("click",()=>{

    torres = JSON.parse(JSON.stringify(estadoInicial));
    movimientos = 0;
    origen = null;

    renderizar();
});

renderizar();