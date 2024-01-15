const info = document.getElementById("toast-info")
// Después de 3000 milisegundos (3 segundos), inicia la animación de desaparición
setTimeout(function () {
    // Inicia la animación de desaparición
    info.style.opacity = 0;
}, 3000);

// Configura el evento de transición
info.addEventListener("transitionend", function (event) {
    // Verifica que la transición sea en la propiedad de opacidad
    if (event.propertyName === "opacity") {
        // Oculta el toast después de la animación
        info.style.display = "none";
    }
});