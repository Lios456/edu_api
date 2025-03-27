from django.contrib.auth.backends import BaseBackend
from .models import Pariente

class ParienteAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            pariente = Pariente.objects.get(numero_identificacion=username)
            if password == pariente.numero_identificacion:
                return pariente
        except Pariente.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Pariente.objects.get(pk=user_id)
        except Pariente.DoesNotExist:
            return None