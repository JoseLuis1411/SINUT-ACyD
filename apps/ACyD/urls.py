from django.urls import path
from . import views

urlpatterns = [
    path('homealumno/', views.alumno_home, name='homealumno'),
    path('homeprofesor/', views.profesor_home, name='homeprofesor'),
    path('homeadmin/', views.admin_home, name='homeadmin'),
    path('homeculturales/', views.culturaes_home, name='homeculturales'),
]