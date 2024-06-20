from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import  HttpResponse

#para mis funciones ACtD
from django.contrib import messages
from apps.Usuario.models import usuarios

from django.contrib.auth import logout

def menu(request):
    return render (request, "menu.html")

def login(request):
    return render (request, "login.html")
    
#views alumnos
def indexalumno(request):
    return render (request, "alumnos/indexalumno.html")
def procesosalumno(request):
    return render (request, "alumnos/procesosalumno.html")
def reportesalumno(request):
    return render (request, "alumnos/reportesalumno.html")

#views procesos alumnos
def pagosalumno(request):
    return render (request, "alumnos/procesos/pagos.html")
def cambiopass(request):
    return render (request, "alumnos/procesos/cambiopass.html")
def editdatosalumno(request):
    return render (request, "alumnos/procesos/editdatosalumno.html")
def reinscripcionlinea(request):
    return render (request, "alumnos/procesos/reinscripcionlinea.html")

#views reportes alumnos
def adeudosalumno(request):
    return render (request, "alumnos/reportes/adeudosalumno.html")
def boletas(request):
    return render (request, "alumnos/reportes/boletas.html")
def documentacionelec(request):
    return render (request, "alumnos/reportes/documentacionelec.html")
def historialpagos(request):
    return render (request, "alumnos/reportes/historialpagos.html")



#views ACyD
# Vista del login para ACyD
def loginACyD(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Buscar usuario en la tabla 'usuarios'
        try:
            user = usuarios.objects.get(usuario=username)
        except usuarios.DoesNotExist:
            user = None
        
        if user is not None:
            # Verificar la contraseña
            if password == user.contraseña:
                # Contraseña correcta, guardar datos en la sesión manualmente
                request.session['user_id'] = user.idUsuario
                request.session['user_type'] = user.idTipoUsuario_id
                
                # Redirigir según el tipo de usuario
                if user.idTipoUsuario_id == 6:
                    next_url = request.GET.get('next', '/homealumno/')
                    return redirect(next_url)
                elif user.idTipoUsuario_id == 4:
                    next_url = request.GET.get('next', '/homeprofesor/')
                    return redirect(next_url)
                elif user.idTipoUsuario_id == 33:
                    next_url = request.GET.get('next', '/homeadmin/')
                    return redirect(next_url)
                elif user.idTipoUsuario_id == 25:
                    next_url = request.GET.get('next', '/homeculturales/')
                    return redirect(next_url)
                else:
                    messages.error(request, 'Tipo de usuario no reconocido')
                    return redirect('/LoginACyD/')
            else:
                # Contraseña incorrecta
                messages.error(request, 'Usuario o contraseña incorrectos')
                return redirect('/LoginACyD/')
        else:
            # Usuario no encontrado
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('/LoginACyD/')
    
    return render(request, 'loginACyD.html')

def logout_view(request):
    logout(request)
    return redirect('/LoginACyD/')