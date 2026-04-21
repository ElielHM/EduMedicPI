const edit = document.getElementById('edit');
const pfp = document.getElementById('pfp')
const password = document.getElementById("password");

    edit.addEventListener('mouseenter', mostrarEdit);
    edit.addEventListener('mouseleave', ocultarEdit);

    function mostrarEdit(){
        edit.classList.add('show')
    }

    function ocultarEdit(){
        edit.classList.remove('show')
    }

    function mostrarPass() {
         var input = document.getElementById("password");
            if (input.type === "password") {
            input.type = "text";
        } else {
            input.type = "password";
        }
    }