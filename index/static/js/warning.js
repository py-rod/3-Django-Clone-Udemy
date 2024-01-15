const warning = document.getElementById("toast-warning")
// Después de 3000 milisegundos (3 segundos), inicia la animación de desaparición
setTimeout(function () {
    // Inicia la animación de desaparición
    warning.style.opacity = 0;
}, 3000);

// Configura el evento de transición
warning.addEventListener("transitionend", function (event) {
    // Verifica que la transición sea en la propiedad de opacidad
    if (event.propertyName === "opacity") {
        // Oculta el toast después de la animación
        warning.style.display = "none";
    }
});