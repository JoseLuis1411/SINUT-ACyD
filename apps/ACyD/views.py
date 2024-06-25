from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from functools import wraps

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


#registro de actividades 


def registro_actividades(request):
    return render(request, 'ACyD/registroActividades.html')