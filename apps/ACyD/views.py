from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from functools import wraps
from .models import dias, horarios, actividadesACyD
from apps.Empleado.models import empleados
from apps.Alumno.models import periodo

# Create your views here.

def login_required_custom(user_type=None):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if 'user_id' not in request.session:
                return redirect('/LoginACyD/?next=' + request.path)
            if user_type is not None and request.session.get('user_type') != user_type:
                return redirect('/LoginACyD/')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

@login_required_custom(user_type=6)
def alumno_home(request):
    return render(request, 'ACyD/alumnoACyD.html')

@login_required_custom(user_type=4)
def profesor_home(request):
    return render(request, 'ACyD/profesorACyD.html')

@login_required_custom(user_type=33)
def admin_home(request):
    return render(request, 'ACyD/adminACyD.html')   

@login_required_custom(user_type=25)
def culturaes_home(request):
    return render(request, 'ACyD/culturalesACyD.html')  


                                        #registro de actividades#

#funcion para llenar los desplegables del formulario de registro
def registro_actividades(request):
    Dias = dias.objects.all() #metraigo los dias de la base de datos
    Horarios = horarios.objects.all()
    Maestros = empleados.objects.all() #me traigo todos los empleados un sin filtras solo los maestros de extracurriculares
    Periodos = periodo.objects.all() #me traigo todos los periodos sin hacer ningun filtro aun 
    return render(request, 'ACyD/agregarActividades.html', {'Dias':Dias, 'Horarios': Horarios, 'Maestros': Maestros, 'Periodos': Periodos})

#funcion para guardar la actividad con los datos que se reciban del POST
#Ahora solo guarda de una por una falta la programacion para que guarde las de todo un dia 
def guardar_actividades(request):
    actividad = request.POST['txtActividad']
    cupo = request.POST['numCupo']
    idMaestro = request.POST['IdMaestro']
    idDia = request.POST['IdDia']
    idHorario = request.POST['IdHorario']
    idPeriodo = request.POST['IdPeriodo']
    
    actividad = actividadesACyD.objects.create(
        actividad=actividad,
        cupo=cupo,
        idMaestro=idMaestro,
        idDia=idDia,
        idHorario=idHorario,
        idPeriodo=idPeriodo
    )
    
    #Variable para que se compruebe si se guardo o no la actividad en la base de datos si es 1 se guardo correctamete
    guardada = 0
    
    if actividad:
        guardada = 1

    return render(request, 'ACyD/actividadesRegistradas.html' , {'guardada', guardada})


def mostrar_actividades(request):
    return render(request, 'ACyD/actividadesRegistradas.html') 
