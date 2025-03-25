
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Usuario

class UsuarioCreationForm(forms.ModelForm):
    """
    Formulario para crear nuevos usuarios.
    Incluye dos campos de contraseña para confirmación.
    """
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('usuario', 'email', 'nombre', 'apellido', 'personal')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        # Se llama al setter de password (que en este caso asigna el valor a 'clave')
        user.password = self.cleaned_data["password1"]
        if commit:
            user.save()
        return user

class UsuarioChangeForm(forms.ModelForm):
    """
    Formulario para actualizar usuarios.
    Reemplaza el campo de contraseña por uno de solo lectura.
    """
    password = ReadOnlyPasswordHashField(
        label="Contraseña",
        help_text=("Puede cambiar la contraseña utilizando "
                   "el <a href=\"../password/\">formulario de cambio de contraseña</a>.")
    )

    class Meta:
        model = Usuario
        fields = ('usuario', 'email', 'nombre', 'apellido', 'password', 'personal', 'estado', 'es_superadmin')

    def clean_password(self):
        # Devuelve siempre el valor inicial.
        return self.initial["password"]
