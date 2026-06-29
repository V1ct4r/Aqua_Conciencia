from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear-cuenta/', views.crear_cuenta, name='crear_cuenta'),
    path('restablecer/', views.restablecer, name='restablecer'),
    path('nueva-contraseña/', views.nueva_contraseña, name='nueva_contraseña'),
    path('comuna/<str:nombre>/', views.comuna, name='comuna'),
    path('ayuda/', views.ayuda, name='ayuda'),

    path('panel/', views.panel, name='panel'),
    
    # QUIZZES
    path('quiz/', views.quiz, name='quiz_inicio'),

    # Quiz 1
    path('quiz1/<int:numero>/', views.quiz1, name='quiz1'),
    path('quiz1/resultado/', views.resultado_quiz1, name='resultado_quiz1'),

    # Quiz 2
    path('quiz2/<int:numero>/', views.quiz2, name='quiz2'),
    path('quiz2/resultado/', views.resultado_quiz2, name='resultado_quiz2'),

    # Quiz 3
    path('quiz3/<int:numero>/', views.quiz3, name='quiz3'),
    path('quiz3/resultado/', views.resultado_quiz3, name='resultado_quiz3'),

    # Quiz 4
    path('quiz4/<int:numero>/', views.quiz4, name='quiz4'),
    path('quiz4/resultado/', views.resultado_quiz4, name='resultado_quiz4'),

    # Quiz 5
    path('quiz5/<int:numero>/', views.quiz5, name='quiz5'),
    path('quiz5/resultado/', views.resultado_quiz5, name='resultado_quiz5'),

    # Quiz 6
    path('quiz6/<int:numero>/', views.quiz6, name='quiz6'),
    path('quiz6/resultado/', views.resultado_quiz6, name='resultado_quiz6'),

    # Quiz 7
    path('quiz7/<int:numero>/', views.quiz7, name='quiz7'),
    path('quiz7/resultado/', views.resultado_quiz7, name='resultado_quiz7'),

    # Quiz 8
    path('quiz8/<int:numero>/', views.quiz8, name='quiz8'),
    path('quiz8/resultado/', views.resultado_quiz8, name='resultado_quiz8'),

    # Quiz 9
    path('quiz9/<int:numero>/', views.quiz9, name='quiz9'),
    path('quiz9/resultado/', views.resultado_quiz9, name='resultado_quiz9'),

    # Quiz 10
    path('quiz10/<int:numero>/', views.quiz10, name='quiz10'),
    path('quiz10/resultado/', views.resultado_quiz10, name='resultado_quiz10'),

    # Quiz 11
    path('quiz11/<int:numero>/', views.quiz11, name='quiz11'),
    path('quiz11/resultado/', views.resultado_quiz11, name='resultado_quiz11'),

    # Quiz 12
    path('quiz12/<int:numero>/', views.quiz12, name='quiz12'),
    path('quiz12/resultado/', views.resultado_quiz12, name='resultado_quiz12'),

    # Otras secciones
    path('noticias/', views.noticias, name='noticias'),
    path('foro/', views.foro, name='foro'),
    path('perfil/', views.perfil, name='perfil'),
    path('configuracion/', views.configuracion, name='configuracion'),

    # 🔹 Nuevas rutas
    path('borrar_cuenta/', views.borrar_cuenta, name='borrar_cuenta'),
    path('logout/', views.logout_usuario, name='logout_usuario'),
]
