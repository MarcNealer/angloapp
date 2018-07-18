from django.shortcuts import render
from .models import History
# Create your views here.


def historyselect(request):
    grupo = list(set(History.objects.all().values_list('nombre', flat=True)))
    alumno = list(set([x.alumno for x in History.objects.all()]))
    return render(request, 'history/select.html', {'grupo': grupo, 'alumno': alumno})

def historygrupo(request):
    recs = History.objects.filter(nombre=request.GET['grupo']).order_by('created')
    return render(request, 'history/history.list.html', {'records':recs})

def historyalumno(request):
    recs = History.objects.filter(alumno__id=request.GET['alumno']).order_by('created')
    return render(request, 'history/history.list.html', {'records':recs})

def historyall(request):
    recs = History.objects.all().order_by('created')
    return render(request, 'history/history.list.html', {'records':recs})