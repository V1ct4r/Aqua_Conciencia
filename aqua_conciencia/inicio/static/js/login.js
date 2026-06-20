// Se agrega codigo para el enmascaramiento de contraseña

function togglePassword() {
    const input = document.getElementById('password');
    if (input.type === 'password') {
        input.type = 'text';
    } else {
        input.type = 'password';
    }
}