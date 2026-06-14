from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear-cuenta/', views.crear_cuenta, name='crear_cuenta'),
    path('restablecer/', views.restablecer, name='restablecer'),

    path('panel/', views.panel, name='panel'),
    path('quiz/', views.quiz, name='quiz'),

    path('noticias/', views.noticias, name='noticias'),
    path('foro/', views.foro, name='foro'),
    path('perfil/', views.perfil, name='perfil'),
    path('configuracion/', views.configuracion, name='configuracion'),
]