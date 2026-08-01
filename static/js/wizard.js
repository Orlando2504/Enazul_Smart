let pasoActual = 1;

function mostrarPaso(numeroPaso) {

    // Ocultar todos
    document.getElementById("contenedor-paso1").style.display = "none";
    document.getElementById("contenedor-paso2").style.display = "none";
    document.getElementById("contenedor-paso3").style.display = "none";

    // Mostrar el solicitado
    document.getElementById("contenedor-paso" + numeroPaso).style.display = "block";

    pasoActual = numeroPaso;

    actualizarBarra();
}