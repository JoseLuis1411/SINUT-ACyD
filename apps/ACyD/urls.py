from django.urls import path
from . import views

urlpatterns = [
    path('homealumno/', views.alumno_home, name='homealumno'),
    path('homeprofesor/', views.profesor_home, name='homeprofesor'),
    path('homeadmin/', views.admin_home, name='homeadmin'),
    path('homeculturales/', views.culturaes_home, name='homeculturales'),
    path('registroActs/', views.registro_actividades, name='registroActs'),
    path('guardarActividades/', views.guardar_actividades, name='guardarActividades'),
]