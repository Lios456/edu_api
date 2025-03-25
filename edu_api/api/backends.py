from django.contrib.auth.backends import BaseBackend
from .models import Pariente

class ParienteAuthBackend(BaseBackend):
    def authenticate(self, request, numero_identificacion=None):
        try:
            return Pariente.objects.get(numero_identificacion=numero_identificacion)
        except Pariente.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Pariente.objects.get(pk=user_id)
        except Pariente.DoesNotExist:
            return None