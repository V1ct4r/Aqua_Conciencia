from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
def inicio(request):

    if request.method == 'POST':
        usuario = request.POST['usuario']
        password = request.POST['password']

        user = authenticate(
            request,
            username=usuario,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/panel/')
    
    return render(request, 'inicio/login.html')
def restablecer(request):
    return render(request, 'inicio/restablecer_contraseña.html')


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


def error_404(request, exception):
    return render(request, 'inicio/error_404.html', status=404)
from django.contrib.auth import authenticate, login
def panel(request):
    return render(request, 'inicio/panel.html')

def noticias(request):
    return render(request, 'inicio/noticias.html')

def foro(request):
    return render(request, 'inicio/foro.html')

def perfil(request):
    return render(request, 'inicio/perfil.html', {'usuario': request.user})

def configuracion(request):
    return render(request, 'inicio/configuracion.html')

from django.contrib.auth import authenticate, login, logout

def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')

def borrar_cuenta(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
      
        if password != confirm_password:
            return render(request, 'inicio/borrar_cuenta.html', {
                'error': 'Las contraseñas no coinciden'
            })
        
        if request.user.check_password(password):
            request.user.delete()      
            logout(request)             
            return redirect('inicio')   
        else:
            return render(request, 'inicio/borrar_cuenta.html', {
                'error': 'Contraseña incorrecta'
            })
    
    return render(request, 'inicio/borrar_cuenta.html')

def comuna(request, nombre):
    return render(request, f'inicio/comuna_{nombre}_mapa.html')