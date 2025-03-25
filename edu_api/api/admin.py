from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Usuario
from .forms import UsuarioCreationForm, UsuarioChangeForm

class UsuarioAdmin(BaseUserAdmin):
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm

    list_display = ('usuario', 'email', 'nombre', 'apellido', 'estado', 'es_superadmin')
    list_filter = ('estado', 'es_superadmin')
    fieldsets = (
        (None, {'fields': ('usuario', 'clave')}),
        ('Información personal', {'fields': ('nombre', 'apellido', 'email', 'personal')}),
        # Solo mostramos los campos reales de la base de datos.
        ('Permisos', {'fields': ('estado', 'es_superadmin')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('usuario', 'email', 'nombre', 'apellido', 'personal', 'password1', 'password2'),
        }),
    )
    search_fields = ('usuario', 'email', 'nombre', 'apellido')
    ordering = ('usuario',)
    filter_horizontal = ()

admin.site.register(Usuario, UsuarioAdmin)

admin.site.style = 'dark'
admin.site.site_header = 'Administración de EduControl'
admin.site.site_title = 'EduControl'
admin.site.index_title = 'Panel de administración'
admin.site.site_url = '/admin/'
