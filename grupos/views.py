from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Grupo, Alumno, Membership, Idioma
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.urls import reverse
from history.utils import history_add

class MemberCreate(CreateView):
    model = Membership
    fields = '__all__'

class MemberListView(generic.ListView):
    model = Membership

def grupos_list(request):
    query = request.GET.get('q', None)
    qs = Grupo.objects.all().order_by('nombre') 
    if query is not None:
        qs = qs.filter(
                Q(nombre__icontains=query) |
                Q(idioma__name=query) |
                Q(nivel__name=query) |
                Q(horario__name=query) |
                Q(salon__name=query) |
                Q(profesor__name=query) 
                )
                
    context =  {
        "object_list": qs,
    }
    template = 'grupos/grupo_list.html'
    return render(request, template, context) 
    
class GrupoDetailView(generic.DetailView):
    model = Grupo
    
def alumnos_list(request):
    query = request.GET.get('q', None)
    qs = Alumno.objects.all().order_by('nombre') 
    if query is not None:
        qs = qs.filter(
                Q(nombre__icontains=query) |
                Q(apaterno__icontains=query) |
                Q(amaterno__icontains=query) |
                Q(cel__icontains=query) |
                Q(tel__icontains=query) 
                )
                
    context =  {
        "object_list": qs,
    }
    template = 'grupos/alumno_list.html'
    return render(request, template, context) 
    
class AlumnoDetailView(generic.DetailView):
    model = Alumno
    
class GrupoCreate(CreateView):
    model = Grupo
    fields = ['nombre', 'fecha_inicio', 'idioma', 'nivel', 'horario', 'profesor', 'salon',]
    
class AlumnoCreate(CreateView):
    model = Alumno
    fields = '__all__'
    
class AlumnoUpdate(UpdateView):
    model = Alumno
    fields = ['grupo',]
    template_name ='grupos/agregar_alumno_a_grupo.html'
    
    def get_context_data(self, **kwargs):
        """
        Add associated alumno to form template so can display its name in HTML.
        """
        # Call the base implementation first to get a context
        context = super(AlumnoUpdate, self).get_context_data(**kwargs)
        # Get the alumno from id and add it to the context
        context['alumno'] = get_object_or_404(Alumno, pk = self.kwargs['pk'])
        return context        

    def get_success_url(self): 
        """
        After posting comment return to associated blog.
        """
        return reverse('alumno-detail', kwargs={'pk': self.kwargs['pk'],})

def remover(request, pk1, pk2):
            
    a = Alumno.objects.get(id=pk1) # get an article that matches that id and return it into  variable a
    b = Grupo.objects.get(id=pk2)
    a.grupo.remove(b)
    history_add(b,a, 'Bajas')

    return HttpResponseRedirect(reverse('grupo-detail', args=(pk2,)))
    
def remover_grupo(request, pk1, pk2):
        #remueve la relacion del grupo desde el detalle del alumno y regresa a ese mismo detalle de alumno   
    a = Alumno.objects.get(id=pk1) # get an article that matches that id and return it into  variable a
    b = Grupo.objects.get(id=pk2)
    a.grupo.remove(b)
    history_add(b,a, 'Bajas')

    return HttpResponseRedirect(reverse('alumno-detail', args=(pk1,)))
    

#PRUEBAS PARA Membership
   

def remover_miembro(request, pk):
    
        #remueve la relacion del grupo desde el detalle del alumno y regresa a ese mismo detalle de alumno 
    m = Membership.objects.get(id=pk) # get an article that matches that id and return it into  variable a
    m.delete()
    history_add(m.grupo, m.alumno, 'Bajas')


    return HttpResponseRedirect(reverse('Bajas'))
    
#Para cambiar de status 'pre-inscrito' a 'inscrito' Membership
def inscribir(request, pk):
    m = Membership.objects.get(id=pk) # get an article that matches that id and return it into  variable a
    m.status = 'i'
    m.save() #save to the model
    history_add(m.grupo, m.alumno, 'inscribir')

    return HttpResponseRedirect(reverse('grupos'))
    