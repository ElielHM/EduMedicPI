from django import forms
from .models import usuario, medicamento, nota, libro

class UsuarioLoginForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ['email','password']        

class BuscarMedicamento(forms.ModelForm):
    class Meta:
        model = medicamento
        fields = ['nombre','uso']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].required = False
        self.fields['uso'].required = False

class BuscarLibro(forms.ModelForm):
    class Meta:
        model = libro
        fields = ['titulo','categoria']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titulo'].required = False


class NuevaNota(forms.ModelForm):
    class Meta:
        model = nota
        fields = ['titulo','contenido']

class RegistrarUser(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ['nombreUser','email','password']

class NuevaImagen(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ['id','imagenPerfil']

class AgregarLibro(forms.ModelForm):
    class Meta:
        model = libro
        fields = ['titulo','autor','isbn','fecha','categoria','url','portada']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['autor'].required = False
        self.fields['isbn'].required = False
        self.fields['fecha'].required = False
        self.fields['portada'].required = False