from django.shortcuts import render

# Create your views here.
def alumno_home(request):
    return render(request, 'ACyD/alumnoACyD.html')

def profesor_home(request):
    return render(request, 'ACyD/profesorACyD.html')

def admin_home(request):
    return render(request, 'ACyD/adminACyD.html')   

def culturaes_home(request):
    return render(request, 'ACyD/culturalesACyD.html')  