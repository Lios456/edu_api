from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import Pariente

class ParienteJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            pariente_id = validated_token.get('pariente_id')
            if pariente_id:
                pariente = Pariente.objects.get(pk=pariente_id)
                if not pariente.is_active:  # Use the property we defined
                    raise AuthenticationFailed('User inactive', code='user_inactive')
                return pariente
            raise AuthenticationFailed('Token inválido')
        except Pariente.DoesNotExist:
            raise AuthenticationFailed('Usuario no encontrado')