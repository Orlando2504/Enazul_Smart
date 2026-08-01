document.addEventListener("DOMContentLoaded", () => {

    actualizarBarra();

    // ==========================
    // PASO 1
    // ==========================

    const formularioPaso1 = document.getElementById("paso1");

    if (formularioPaso1) {

        formularioPaso1.addEventListener("submit", function (e) {

            e.preventDefault();

            if (!validarPaso1()) {
                this.reportValidity();
                return;
            }

            const datos = {

                tipoDocumento: document.getElementById("tipo_documento").value,
                documento: document.getElementById("documento").value,
                nombre: document.getElementById("nombre").value,
                edad: document.getElementById("edad").value,
                celular: document.getElementById("celular").value,
                correo: document.getElementById("correo").value

            };

            guardar("paso1", datos);

            mostrarPaso(2);

        });

    }

    // ==========================
    // PASO 2
    // ==========================

    const formularioPaso2 = document.getElementById("paso2");

    if (formularioPaso2) {

        const institucion = document.getElementById("institucion");

        if (institucion) {

            institucion.addEventListener("change", function () {

                const bloque = document.getElementById("portaArmaDiv");

                if (!bloque) return;

                if (this.value === "PNP") {

                    bloque.style.display = "block";

                } else {

                    bloque.style.display = "none";

                    const combo = document.getElementById("porta_arma");

                    if (combo) combo.value = "No";

                }

            });

        }

        formularioPaso2.addEventListener("submit", function (e) {

            e.preventDefault();

            if (!validarPaso2()) {

                this.reportValidity();

                return;

            }

            const datos = {

                institucion: document.getElementById("institucion").value,
                contrato: document.getElementById("contrato").value,
                antiguedad: document.getElementById("antiguedad").value,
                ingreso: document.getElementById("ingreso").value,
                portaArma: document.getElementById("porta_arma")
                    ? document.getElementById("porta_arma").value
                    : "No"

            };

            guardar("paso2", datos);

            mostrarPaso(3);

        });

    }

    // ==========================
    // BOTÓN VOLVER
    // ==========================

    const volverPaso1 = document.getElementById("volverPaso1");

    if (volverPaso1) {

        volverPaso1.addEventListener("click", () => {

            mostrarPaso(1);

        });

    }

    const volverPaso2 = document.getElementById("volverPaso2");

    if (volverPaso2) {

        volverPaso2.addEventListener("click", () => {

            mostrarPaso(2);

        });

    }

    // ==========================
    // PASO 3
    // ==========================

    const formularioPaso3 = document.getElementById("paso3");

    if (formularioPaso3) {

        formularioPaso3.addEventListener("submit", async function (e) {

            e.preventDefault();

            const paso1 = recuperar("paso1");
            const paso2 = recuperar("paso2");

            const solicitud = {

                nombre: paso1.nombre,

                documento: paso1.documento,

                celular: paso1.celular,

                correo: paso1.correo,

                edad: parseInt(paso1.edad),

                ingreso: parseFloat(paso2.ingreso),

                contrato: paso2.contrato,

                institucion: paso2.institucion,

                antiguedad: parseInt(paso2.antiguedad),

                entidades: parseInt(document.getElementById("entidades").value),

                perdidas: parseInt(document.getElementById("perdidas").value),

                porta_arma: paso2.portaArma

            };

            console.log("Solicitud enviada:");

            console.log(solicitud);

            try {

                const respuesta = await fetch("/evaluar", {

                    method: "POST",

                    headers: {

                        "Content-Type": "application/json"

                    },

                    body: JSON.stringify(solicitud)

                });

                if (!respuesta.ok) {

                    throw new Error("Error HTTP " + respuesta.status);

                }

                const resultado = await respuesta.json();

                console.log(resultado);

                sessionStorage.setItem(
                    "resultado",
                    JSON.stringify(resultado)
                );

                window.location.href = "/resultado";

                // Próximo Sprint:
                // window.location.href="/resultado";

            }

            catch (error) {

                console.error(error);

                alert("No fue posible conectar con el servidor.");

            }

        });

    }

});