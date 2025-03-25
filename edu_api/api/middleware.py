from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import Pariente

class ParienteJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            pariente_id = validated_token.get('pariente_id')
            return Pariente.objects.get(pk=pariente_id)
        except Pariente.DoesNotExist:
            raise AuthenticationFailed('Pariente no encontrado')