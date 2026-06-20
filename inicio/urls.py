from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('restablecer/', views.restablecer, name='restablecer'),
    path('nueva-contrasena/', views.nueva_contraseña, name='nueva_contraseña'),

    path('crear-cuenta/', views.crear_cuenta, name='crear_cuenta'),

    path('panel/', views.panel, name='panel'),
    path('noticias/', views.noticias, name='noticias'),
    path('foro/', views.foro, name='foro'),
    path('perfil/', views.perfil, name='perfil'),
    path('configuracion/', views.configuracion, name='configuracion'),

    path('quiz/', views.quiz, name='quiz'),
]