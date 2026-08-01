function guardar(nombre, datos){

    localStorage.setItem(nombre, JSON.stringify(datos));

}

function recuperar(nombre){

    const datos = localStorage.getItem(nombre);

    return datos ? JSON.parse(datos) : null;

}