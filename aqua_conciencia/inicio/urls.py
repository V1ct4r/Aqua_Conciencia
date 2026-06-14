from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear-cuenta/', views.crear_cuenta, name='crear_cuenta'),
    path('restablecer/', views.restablecer, name='restablecer'),
]

handler404 = 'inicio.views.error_404'