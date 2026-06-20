from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password


def inicio(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        password = request.POST['password']

        user = authenticate(request, username=usuario, password=password)

        if user is not None:
            login(request, user)
            return redirect('/panel/')

    return render(request, 'inicio/login.html')


def restablecer(request):
    return render(request, 'inicio/restablecer_contraseña.html')


# 🔥 MODIFICADO SOLO ESTO (IMPORTANTE)
def nueva_contraseña(request):
    return render(request, 'inicio/nueva_contraseña.html')


def crear_cuenta(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        usuario = request.POST['usuario']
        password = request.POST['password']

        User.objects.create_user(
            username=usuario,
            email=correo,
            password=password
        )

        return redirect('inicio')

    return render(request, 'inicio/creacion_cuenta.html')


def panel(request):
    return render(request, 'inicio/panel.html')


def noticias(request):
    return render(request, 'inicio/noticias.html')


def foro(request):
    return render(request, 'inicio/foro.html')


def perfil(request):
    return render(request, 'inicio/perfil.html')


def configuracion(request):
    return render(request, 'inicio/configuracion.html')


def quiz(request):
    return render(request, 'inicio/quiz.html')


def error_404(request, exception):
    return render(request, 'inicio/error_404.html', status=404)