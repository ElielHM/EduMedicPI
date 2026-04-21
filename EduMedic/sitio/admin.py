from django.contrib import admin
from .models import medicamento, libro, usuario, nota

class AdminModel(admin.ModelAdmin):
    readonly_fields=('id','created','updated')
    list_display=('id','nombre','riesgo')
    list_editable=['riesgo']
    date_hierarchy='created' 
    list_filter = ['riesgo']
    

class AdminLibro(admin.ModelAdmin):
    readonly_fields=('id','created','updated')
    date_hierarchy='created'     
    
class AdminUser(admin.ModelAdmin):
    readonly_fields=('id','created','updated')
    date_hierarchy='created'

class AdminNota(admin.ModelAdmin):
    readonly_fields=('id','created','updated')
    date_hierarchy='created'

admin.site.register(medicamento,AdminModel)
admin.site.register(libro,AdminLibro)
admin.site.register(usuario,AdminUser)
admin.site.register(nota,AdminNota)

