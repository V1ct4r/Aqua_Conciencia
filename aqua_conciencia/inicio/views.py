from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio/login.html')

def restablecer(request):
    return render(request, 'inicio/restablecer_contraseña.html')
def crear_cuenta(request):
    return render(request, 'inicio/creacion_cuenta.html')
def error_404(request, exception):
    return render(request, 'inicio/error_404.html', status=404)