from django.shortcuts import render, redirect, get_object_or_404
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
    #instancias
    Dias = dias.objects.all() #metraigo los dias de la base de datos
    Horarios = horarios.objects.all()
<<<<<<< HEAD
    Maestros = empleados.objects.all() #me traigo todos los empleados un sin filtras solo los maestros de extracurriculares
    Periodos = periodo.objects.all() #me traigo todos los periodos sin hacer ningun filtro aun 
=======
    Maestros = empleados.objects.filter(idArea=2) #me traigo todos los empleados un sin filtras solo los maestros de extracurriculares
    Periodos = periodo.objects.all().order_by('-idPeriodo') #me traigo todos los periodos sin hacer ningun filtro aun 
>>>>>>> 7052231afafed41c728917abf41a0ce677e544e2
    return render(request, 'ACyD/agregarActividades.html', {'Dias':Dias, 'Horarios': Horarios, 'Maestros': Maestros, 'Periodos': Periodos})

#funcion para guardar la actividad con los datos que se reciban del POST
#Ahora solo guarda de una por una falta la programacion para que guarde las de todo un dia 
def guardar_actividades(request):
    
    #Si se va guardar alguna actividad entra el if
    if request.method == 'POST':
        actividad = request.POST.get('nombre')
        cupo = request.POST.get('cupos')
        id_maestro = request.POST.get('profesor')
        id_Dia = request.POST.get('dia')
        id_horario = request.POST.get('intereses')
        id_periodo = request.POST.get('periodo')
        
        #instancias
        idMaestro = empleados.objects.get(idEmpleado=id_maestro)
        idDia = dias.objects.get(idDia = id_Dia)
        idHorario = horarios.objects.get(idHorario = id_horario)
        idPeriodo = periodo.objects.get(idPeriodo = id_periodo)
        
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

        return render(request, '' , {'guardada': guardada})
    
    #Si entra a la pagina para ver las activiades registradas entra aqui
    else:
        #instancias
        ActiviadesCyD = actividadesACyD.objects.all()
        return render(request, '', {'guardada': 0, 'ActiviadesCyD': ActiviadesCyD})