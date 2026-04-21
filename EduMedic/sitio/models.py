from django.db import models
from ckeditor.fields import RichTextField

class medicamento(models.Model):

    riesgo_opc = [('A','A'),('B','B'),('C','C'),('D','D'),('X','X'),('Desconocido','Desconocido')]
    id= models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=55)
    uso=models.TextField()
    via=models.CharField(max_length=40)
    dosis=models.TextField()
    riesgo=models.CharField(choices=riesgo_opc, null=True, verbose_name='Riesgo en el embarazo')
    caption=models.TextField(verbose_name="Efectos Adversos")
    generalidades=models.TextField()
    created=models.DateTimeField(auto_now=False, auto_now_add=True)
    updated=models.DateTimeField( auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name='Medicamento'
        verbose_name_plural='Medicamentos'
        ordering = ['nombre']
    def __str__(self):
        return self.nombre 
    
    
class libro(models.Model):

    opcion_categoria = [('NA','NA'),('Anatomia','Anatomia'),('Cardiologia','Cardiologia'),('Enfermeria','Enfermeria'),('Farmacologia','Farmacologia'),('Fisiologia','Fisiologia')]
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100)
    autor =models.CharField(max_length=77, null=True, blank=True)
    isbn=models.CharField(max_length=13, default="NA", null=True, blank=True)
    fecha=models.DateField(verbose_name='Fecha de publicación', null=True, blank=True)
    categoria=models.CharField(choices=opcion_categoria)
    url = models.FileField(upload_to='libros/', null=True, blank=True)
    portada = models.ImageField(upload_to='portadas/', null=True, blank=True)
    aprobado = models.BooleanField(default=False)
    created=models.DateTimeField(auto_now=False, auto_now_add=True)
    updated=models.DateTimeField( auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name='Libro'
        verbose_name_plural='Libros'
        ordering = ['-created']
    def __str__(self):
        return self.titulo     
    

class usuario(models.Model):
    roles=[('Usuario','Usuario'),('Admin','Admin')]
    id=models.AutoField(primary_key=True, unique=True)
    nombreUser=models.CharField(max_length=55)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    imagenPerfil=models.ImageField(upload_to='imagenes/', null=True, blank=True, default='defaults/user.png')
    rol=models.CharField(choices=roles,default='Usuario')
    created=models.DateTimeField(auto_now=False, auto_now_add=True)
    updated=models.DateTimeField( auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
        ordering = ['-created']
    def __str__(self):
        return self.nombreUser   
    
class nota(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100)
    contenido=RichTextField(default='')
    usuario=models.ForeignKey(usuario, to_field='id' ,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now=False, auto_now_add=True)
    updated=models.DateTimeField( auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name='Nota'
        verbose_name_plural='Notas'
        ordering = ['created']
    def __str__(self):
        return self.titulo  