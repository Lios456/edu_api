# urls.py
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # Autenticación
    path('login/', views.CustomTokenObtainPairView.as_view(), name='login'),
    path('loginPadre/', views.ParienteLoginView.as_view()),
    
    path('token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Usuarios
    path('usuario/', views.UsuarioDetailView.as_view(), name='usuario-detail'),
    
    # Parientes
    path('representados/<int:id_pariente>/', views.RepresentadosView.as_view(), name='representados-list'),
    path('detalles/<int:id_estudiante>/', views.DetalleEstudianteView.as_view(), name='detalle-estudiante'),
    path('horario/<int:id_estudiante>/', views.HorarioEstudianteView.as_view(), name='horario-estudiante'),
    
    # Tutores
    path('periodos/', views.PeriodosView.as_view(), name='periodos-list'),
    path('cursos/<int:id_periodo>/', views.CursosView.as_view(), name='cursos-list'),
    path('estudiantes/<int:id_curso>/', views.EstudiantesCursoView.as_view(), name='estudiantes-list'),
    #path('atrasos/', views.AtrasosView.as_view(), name='atrasos-list'),
    #path('atraso/<int:id_atraso>/', views.AtrasosView.as_view(), name='atraso-detail'),
    
    
    # Notificaciones
    path('notificaciones/', views.NotificacionesView.as_view(), name='notificaciones-list'),
    path('notificacion/<int:id>/', views.NotificacionDetailView.as_view(), name='notificacion-detail'),
    
    path('atrasos/', views.AtrasoViewSet.as_view({'get':'list', 'post':'create'}), name='atrasos-list'),
    path('atraso/<int:pk>/', views.AtrasoViewSet.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'}), name='atraso-detail'),
    
    #Materias
    path('paralelos/', views.ParaleloViewSet.as_view(), name='paralelos-list'),
    
    # Rutas para notas
    path('alumno/<int:id_alumno>/notas/', views.NotasAlumnoView.as_view(), name='notas-alumno'),
    path('alumno/<int:id_alumno>/notas/<int:id_periodo>/', views.NotasAlumnoView.as_view(), name='notas-alumno-periodo'),
]