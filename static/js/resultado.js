document.addEventListener("DOMContentLoaded", () => {

    // Si no estamos en la página de resultado, salir
    if (!document.getElementById("estado")) {
        return;
    }

    const datos = sessionStorage.getItem("resultado");

    if (!datos) {
        window.location.href = "/formulario";
        return;
    }

    const resultado = JSON.parse(datos);

    document.getElementById("estado").innerText = resultado.estado;
    document.getElementById("score").innerText = resultado.score + " / 100";
    document.getElementById("riesgo").innerText = resultado.riesgo;

    const lista = document.getElementById("observaciones");

    lista.innerHTML = "";

    const mensajes =
        resultado.estado === "PRECALIFICA"
            ? resultado.observaciones
            : resultado.errores;

    mensajes.forEach(texto => {

        const li = document.createElement("li");

        li.className = "list-group-item";

        li.innerHTML = "✔ " + texto;

        lista.appendChild(li);

    });

});