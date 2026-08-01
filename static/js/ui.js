function actualizarBarra() {

    const barra = document.getElementById("barraProgreso");
    const texto = document.getElementById("textoPaso");

    if (pasoActual === 1) {

        barra.style.width = "33%";
        texto.innerHTML = "Paso 1 de 3";

    }

    if (pasoActual === 2) {

        barra.style.width = "66%";
        texto.innerHTML = "Paso 2 de 3";

    }

    if (pasoActual === 3) {

        barra.style.width = "100%";
        texto.innerHTML = "Paso 3 de 3";

    }

}