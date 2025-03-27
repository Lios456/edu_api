from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from .models import Pariente
def create_jwt_tokens(user):
    refresh = RefreshToken()
    access = AccessToken()
    
    if isinstance(user, Pariente):
        refresh['pariente_id'] = str(user.id)
        access['pariente_id'] = str(user.id)
        access['user_id'] = str(user.id)  # Add standard claim
        access['user_type'] = 'pariente'
    else:
        refresh['user_id'] = str(user.id)
        access['user_id'] = str(user.id) 
        access['user_type'] = 'usuario'
    
    return {
        'access': str(access),
        'refresh': str(refresh),
        'id_pariente': str(user.id),
        'user_type': 'pariente' if isinstance(user, Pariente) else 'usuario',
    }