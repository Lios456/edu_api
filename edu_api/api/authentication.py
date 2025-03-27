from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import Pariente, Usuario

class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        # First try standard claims
        user_id = validated_token.get('user_id')
        user_type = validated_token.get('user_type')
        
        # Fallback to pariente claims if needed
        if not user_id:
            user_id = validated_token.get('pariente_id')
            user_type = 'pariente'

        if user_type == 'pariente':
            try:
                return Pariente.objects.get(pk=user_id)
            except Pariente.DoesNotExist:
                raise AuthenticationFailed('Pariente no encontrado')
        elif user_type == 'usuario':
            try:
                return Usuario.objects.get(pk=user_id)
            except Usuario.DoesNotExist:
                raise AuthenticationFailed('Usuario no encontrado')
        raise AuthenticationFailed('Token inválido')