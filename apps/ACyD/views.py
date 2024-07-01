from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from functools import wraps
from django.db.models import Max, Q
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
    Maestros = empleados.objects.filter(idArea=2) #me solo los empleados que son PA de extracurriculares
    Periodos = periodo.objects.all().order_by('-idPeriodo') #me traigo todos los periodos del mas reciente al mas antiguo
    return render(request, 'ACyD/agregarActividades.html', {'Dias':Dias, 'Horarios': Horarios, 'Maestros': Maestros, 'Periodos': Periodos})

#funcion para guardar la actividad con los datos que se reciban del POST
def guardar_actividades(request):
    #Si se va guardar alguna actividad y existe POST entra el if
    if request.method == 'POST':
        actividad = request.POST.get('nombre')
        cupo = request.POST.get('cupos')
        id_maestro = request.POST.get('profesor')
        id_Dia = request.POST.get('dia')
        #id_horario = request.POST.get('horariosClase')
        id_horarios = request.POST.getlist('horariosClase[]', [])
        id_periodo = request.POST.get('periodo')
        
        #instancias
        idMaestro = empleados.objects.get(idEmpleado=id_maestro)
        idDia = dias.objects.get(idDia = id_Dia)
        idPeriodo = periodo.objects.get(idPeriodo = id_periodo)
        #idHorario = horarios.objects.get(idHorario = id_horario)
        
        for id_horario in id_horarios:
            #instancia
            idHorario = horarios.objects.get(idHorario = id_horario)
            actividad = actividadesACyD.objects.create(
                actividad=actividad,
                cupo=cupo,
                idMaestro=idMaestro,
                idDia=idDia,
                idHorario=idHorario,
                idPeriodo=idPeriodo
            )
            
            #limpio las variables y las lleno nuevamente para que entren bien nuevamente al for
            actividad = None
            cupo = None
            idMaestro = None
            idDia = None
            idPeriodo = None
            idHorario = None
            
            actividad = request.POST.get('nombre')
            cupo = request.POST.get('cupos')
            id_maestro = request.POST.get('profesor')
            id_Dia = request.POST.get('dia')
            #id_horario = request.POST.get('horariosClase')
            #id_horarios = request.POST.getlist('horariosClase[]', [])
            id_periodo = request.POST.get('periodo')
            
            #instancias
            idMaestro = empleados.objects.get(idEmpleado=id_maestro)
            idDia = dias.objects.get(idDia = id_Dia)
            idPeriodo = periodo.objects.get(idPeriodo = id_periodo)
            #idHorario = horarios.objects.get(idHorario = id_horario)
        
        #Variable para que se compruebe si se guardo o no la actividad en la base de datos si es 1 se guardo correctamete
        Guardada = '0'
        
        if actividad:
            Guardada = '1'

        #return render(request, 'ACyD/actividadesRegistradas.html' , {'guardada': guardada})
        return redirect('/actividadesRegistradas/?Guardada' + Guardada)
        
    
    #Si no existe POST
    else:
        
        #return render(request, 'ACyD/actividadesRegistradas.html', {'guardada': 0})
        return redirect('/actividadesRegistradas/?Guardada' + '0')
    
def mostrar_actividades(request):
    #recibo la variable para saber si se guardo o no la consulta que tambien servira para saber si datos se eliminaron o actualizaron
    guardada = request.GET.get('Guardada', '0') # si no recivo get a guardada le asigno 0 
    
    # Obtener el ID máximo de la tabla periodos
    id_periodo_max = periodo.objects.aggregate(max_id=Max('idPeriodo'))['max_id']
    
    #instancias 
    ActsActivas = actividadesACyD.objects.filter(idPeriodo__activo=1)  #me traigo las activiades del periodoactual 
    ActsMaxPeriodo = actividadesACyD.objects.filter(idPeriodo_id=id_periodo_max )#me traigo las activiades del periodo proximo con el Max
    
    # Combinar ambos QuerySets en uno solo
    Acts = ActsActivas.union(ActsMaxPeriodo, all=False) # all=False para asegurar que no haya duplicados 
    
    #mando la variable guardada en 0 para no tener problemas en el html cuando la quiera usar para mandar mensajes de exito
    return render(request, 'ACyD/actividadesRegistradas.html', {'guardada': 0, 'Acts': Acts, 'guardada': guardada})


