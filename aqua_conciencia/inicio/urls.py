from django.urls import path
from . import views 

urlpatterns = [
    path('', views.inicio,
    name='inicio'),]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('restablecer/', views.restablecer, name='restablecer'),
]

handler404 = 'inicio.views.error_404'