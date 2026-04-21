const login = document.getElementById('logInForm');
const password = document.getElementById("password");
const email = document.getElementById('email');
const successMessage = document.getElementById('successMessage');
const validoEmail = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
const NoUsuario = document.getElementById('errorNF');
const errorFin = document.getElementById('errorFin')
const successFin = document.getElementById('successFin')
const successTxt = document.getElementById('successSU')

email.addEventListener('blur', validarEmail);
password.addEventListener("blur", validarPassword);

 const url = window.location.href;

        if(url.includes("signup")){
            const confPassword = document.getElementById('confPassword')
            confPassword.addEventListener('blur', validarConf)
        }

        if (url.includes("errorNA")){
            NoUsuario.textContent = "Usuario no encontrado"
            NoUsuario.classList.add('show')
            errorFin.classList.add('show');
            setTimeout(() => {
            NoUsuario.textContent = ""
            NoUsuario.classList.remove('show')
            errorFin.classList.remove('show');},2000);
        }

        if (url.includes("errorPass")){
            NoUsuario.textContent = "Contraseña incorrecta"
            NoUsuario.classList.add('show')
            errorFin.classList.add('show');
            setTimeout(() => {
            NoUsuario.textContent = ""
            NoUsuario.classList.remove('show')
            errorFin.classList.remove('show');},2000);
        }

        if (url.includes("newUser")){
            successTxt.textContent = "Usuario creado exitosamente"
            successTxt.classList.add('show')
            successFin.classList.add('show');
            setTimeout(() => {
            successTxt.textContent = ""
            successTxt.classList.remove('show')
            successFin.classList.remove('show');},2000);
        }

function validarEmail() {
    const valor = email.value.trim();
    const error = document.getElementById('emailError');
    
    if (!validoEmail.test(valor)) {
        mostrarError(email, error, 'Correo electrónico inválido');
        return false;
    }
    
    ocultarError(email, error);
        return true;
}

function validarConf() {
    const valor1 = password.value.trim();
    const valor2 = confPassword.value.trim();
    const error = document.getElementById('confError');
    
    if (valor1!=valor2) {
        mostrarError(confPassword, error, 'Las contraseñas no coinciden');
        return false;
    }
    
    ocultarError(confPassword, error);
        return true;
}

function validarPassword() {
    const valor = password.value.trim();
    const error = document.getElementById("passwordError");

    if (valor.length < 8) {
        mostrarError(password, error, 'Mínimo 8 carácteres');
        return false;
    }
    if (!/[A-Z]/.test(valor)) {
        mostrarError(password, error, 'Debe contener al menos una mayúscula');
        return false;
    }
    if (!/[0-9]/.test(valor)) {
        mostrarError(password, error, 'Debe contener al menos un número');
        return false;
    }
    ocultarError(password, error);
        return true;
}


   function mostrarPass() {
  var input = document.getElementById("password");
  if (input.type === "password") {
    input.type = "text";
  } else {
    input.type = "password";
  }
}

function mostrarConf() {
  var input = document.getElementById("confPassword");
  if (input.type === "password") {
    input.type = "text";
  } else {
    input.type = "password";
  }
}
   
    

    // Mostrar error
    function mostrarError(input, errorElement, mensaje) {
        input.classList.add('invalid');
        input.classList.remove('valid');
        errorElement.textContent = mensaje;
        errorElement.classList.add('show');
    }

    // Ocultar error
    function ocultarError(input, errorElement) {
        input.classList.remove('invalid');
        input.classList.add('valid');
        errorElement.classList.remove('show');
    }

 login.addEventListener('submit', function(e) {
    e.preventDefault();
    
    const emailValido = validarEmail();
    const passwordValida= validarPassword();

    if(emailValido&&passwordValida){
        const loginData = new FormData(login);
        const success1 = document.getElementById('successIcon')
        const success2 = document.getElementById('successHead')
        const success3 = document.getElementById('successText')


        
        success1.textContent = "✓";
        success2.textContent = "¡Ingreso exitoso!";
        success3.textContent = "Redirecionando al inicio";


        successMessage.classList.add('show');
        
        document.querySelectorAll('.valid').forEach(el => el.classList.remove('valid'));
        
        setTimeout(() => {
            console.log("Login exitoso")
            successMessage.classList.remove('show');
        login.submit();
        },1000);

        
    } 
 })
