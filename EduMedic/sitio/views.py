from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sessions.models import Session
from .models import medicamento, usuario, nota, libro
from .forms import UsuarioLoginForm, BuscarMedicamento, NuevaNota, RegistrarUser, NuevaImagen, BuscarLibro, AgregarLibro
from django.http import HttpResponseForbidden

# Create your views here.
def Principal(request):
    if('idUser' in request.session):
        return render(request,"sitio/home.html")
    return redirect("Login")

def Boot(request):
    if('idUser' in request.session):
        del request.session['idUser']
        del request.session['nombre']
        request.session['pfp'] = './media/defaults/user.png'
    return redirect("AboutUs")

def RV(request):
    if('idUser' in request.session):
        return render(request,'sitio/rv.html')
    return redirect("Login")
def Cortes(request):
    return render(request,"sitio/cortes.html")

def Ayuda(request):
    return render(request,"sitio/ayuda.html")

def Sistemas(request):
    return render(request,"sitio/sistemas.html")

def SIstemaA(request):
    return render(request,"sitio/sistemaA.html")

def SIstemaB(request):
    return render(request,"sitio/sistemaB.html")

def SIstemaC(request):
    return render(request,"sitio/sistemaC.html")

def AboutUs(request):
    return render(request, "sitio/aboutUs.html")
    
def Medicamentos(request):
     if('idUser' in request.session):
        medicamentos=medicamento.objects.all()
        if request.method == 'POST':
            form = BuscarMedicamento(request.POST)
            if(form.is_valid()):
                nombreB = request.POST.get('nombre')
                usoB = request.POST.get('uso')
                if(nombreB != '' and usoB == ''):
                    medicamentos = medicamento.objects.filter(nombre__icontains=nombreB)
                if(usoB != '' and nombreB == ''):
                    medicamentos = medicamento.objects.filter(uso__icontains=usoB)
                if(usoB != '' and nombreB != ''):
                    medicamentos = medicamento.objects.filter(uso__icontains=usoB).filter(nombre__icontains=nombreB)
        return render(request,'sitio/medicamentos.html',{'medicamentos':medicamentos})
     return redirect('Login')

def CrearNota(request):
    return render(request, "sitio/nuevaNota.html")

def Login(request):
    return render(request,"sitio/LogIn.html")

def validarLogin(request):
    if request.method == 'POST':
        form = UsuarioLoginForm(request.POST)
        if(form.is_valid()):
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print("Form Validada")
            try:
                if (usuario.objects.get(email=email)):
                    try:
                        if ( usuario.objects.get(email=email,password=password)):
                            #Si el usuario y password coinciden, enviar al inicio
                            request.session['idUser'] = usuario.objects.get(email=email).id
                            request.session['nombre'] = usuario.objects.get(email=email).nombreUser 
                            request.session['email'] = usuario.objects.get(email=email).email
                            request.session['password'] = usuario.objects.get(email=email).password 
                            request.session['rol'] = usuario.objects.get(email=email).rol
                            request.session['pfp'] = usuario.objects.get(email=email).imagenPerfil.url
                            return redirect("Inicio")
                    except usuario.DoesNotExist:
                        #Si la contraseña no coincide, pero el email si, dar error de contraseña
                        return redirect("NoPass")  
            except usuario.DoesNotExist:
                #Si el email no coincide con el modelo, enviar error de usuario no encontrado
                return redirect("NoUser")   
            #Error si la form no es valida
        return redirect("NoUser")     
    #Enviar a login si se entra a la url sin enviar un form
    return redirect("Login")

def Notas(request):
    if('idUser' in request.session):
        notas=nota.objects.filter(usuario=request.session['idUser'])
        return render(request,'sitio/notas.html',{'notas':notas})
    return redirect('Login')

def NotaNueva(request):
    if request.method=='POST':
        print("Posteado")
        form = NuevaNota(request.POST)
        
        if (form.is_valid()):
            note = form.save(commit=False)
            note.usuario_id = request.session['idUser']
            note.save()
            return redirect("Notas")
    form = NuevaNota()
    return render(request, "sitio/nuevaNota.html", {'form':form})

def EliminarNota(request, id):
    if request.META.get('HTTP_REFERER'):
        notaE = get_object_or_404(nota, id=id)
        notaE.delete()
    return redirect("Notas")

def EditorDeNotas(request, id):
    if request.META.get('HTTP_REFERER'):
        notas = nota.objects.get(id=id)
        return render(request,'sitio/editarNota.html',{'nota':notas})
    return redirect("Notas")

def NotaEditada(request, id):
    notaE = get_object_or_404(nota, id=id)
    form = NuevaNota(request.POST, instance=notaE)
        
    if (form.is_valid()):
        form.save()
        return redirect("Notas")
     
    return render(request, "sitio/editarNota.html", {'nota':notaE})

def Signup(request):
    return render(request,'sitio/signup.html')

def NuevoUser(request):
    if request.method=='POST':
        print("Posteado")
        form = RegistrarUser(request.POST)
        if (form.is_valid()):
            print("Form valida")
            form.save()
            return redirect("Inicio")
    form = RegistrarUser()
    return render(request, "sitio/signup.html", {'form':form})

def Perfil(request):
    if('idUser' in request.session):
        return render(request, 'sitio/perfil.html')
    return redirect('Login')

def cambioImagen(request):
    idSession = request.session['idUser']
    user = usuario.objects.get(id=idSession)
    if request.method=='POST':
        form = NuevaImagen(request.POST, request.FILES, instance=user)        
        if (form.is_valid()):
            pfp = form.save(commit=False)
            pfp.usuario_id = request.session['idUser']
            pfp.save()
            request.session['pfp'] = usuario.objects.get(id=idSession).imagenPerfil.url
            return redirect(Perfil)
    return redirect(Perfil)

def LibrosAdmin(request):
    if request.session['rol'] != 'Admin':
        return redirect("Libros")

    libros=libro.objects.all()
    if request.method == 'POST':
        form = BuscarLibro(request.POST)
        
        if(form.is_valid()):
            tituloL = request.POST.get('titulo')
            categoriaL = request.POST.get('categoria')

            print(tituloL)
            print(categoriaL)
            
            if(tituloL != '' and categoriaL == 'NA'):
               libros = libro.objects.filter(titulo__icontains=tituloL)
               

            if(categoriaL != 'NA' and tituloL == ''):
               libros = libro.objects.filter(categoria__icontains=categoriaL)

            if(tituloL != '' and categoriaL != 'NA'):
               libros = libro.objects.filter(titulo__icontains=tituloL).filter(categoria__icontains=categoriaL)
               
    return render(request,'sitio/librosAdmin.html',{'libros':libros})

def Libros(request):
    if('idUser' in request.session):
        if request.session['rol'] != 'Admin':
            libros=libro.objects.filter(aprobado=True)
            if request.method == 'POST':
                form = BuscarLibro(request.POST)
        
                if(form.is_valid()):
                    tituloL = request.POST.get('titulo')
                    categoriaL = request.POST.get('categoria')
            
                    if(tituloL != '' and categoriaL == 'NA'):
                        libros = libro.objects.filter(titulo__icontains=tituloL, aprobado=True)
               

                    if(categoriaL != 'NA' and tituloL == ''):
                        libros = libro.objects.filter(categoria__icontains=categoriaL, aprobado=True)

                    if(tituloL != '' and categoriaL != 'NA'):
                        libros = libro.objects.filter(titulo__icontains=tituloL).filter(categoria__icontains=categoriaL, aprobado=True)
               
            return render(request,'sitio/libros.html',{'libros':libros})
        else:
            return redirect("LibrosAdmin")
    return redirect('Login')

def AprobarLibro(request, id):
    if request.META.get('HTTP_REFERER'):
        libroA = get_object_or_404(libro, id=id)
        libroA.aprobado = True
        libroA.save()
    return redirect("LibrosAdmin")

def QuitarLibro(request, id):
    if request.META.get('HTTP_REFERER'):
        libroA = get_object_or_404(libro, id=id)
        libroA.aprobado = False
        libroA.save()
    return redirect("LibrosAdmin")

def LibrosNoAprobados(request):
    if request.session['rol'] != 'Admin':
        return redirect("Libros")

    libros=libro.objects.filter(aprobado=False) 
    return render(request,'sitio/librosAdmin.html',{'libros':libros})   

def AgregarLibroV(request):
    return render(request,'sitio/agregarLibro.html')

def NuevoLibro(request):
    if request.method=='POST':
        print("Posteado")
        form = AgregarLibro(request.POST, request.FILES)
        if (form.is_valid()):
            print("Form valida")
            form.save()
            return redirect("Libros")
    form = AgregarLibro()
    return render(request, "sitio/agregarLibro.html", {'form':form})