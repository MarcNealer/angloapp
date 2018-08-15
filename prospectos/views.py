from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Prospecto, ProspectoAccion, ProspectoRazon, Razon, Idioma
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy


class ProspectoDetailView(generic.DetailView):
    model = Prospecto

class IdiomaListView(generic.ListView):
    model = Idioma
    fields = '__all__'
    
    # este IdiomaListView no sirve para sacar los idiomas del SELECT en TODOS LOS PROSPECTOS. Lo que sirvió fue pasar
    # Idioma.objects.all() como contexto en  def prospecto_list_view........

    '''
    def products_list(request):
    products = Product.objects.all()
    order = request.GET.get('order', 'name')  # Set 'name' as a default value
    products = products.order_by(order)
    return render(request, 'products_list.html', {
        'products': products
    })
    
    '''
    
def prospecto_list_view(request):
    query = request.GET.get('q', None)
    qs = Prospecto.objects.all() #.order_by('-pub_date') #por default esta ordenado por mas reciente
    idiomas = Idioma.objects.all()
    accion = ProspectoAccion.objects.all().order_by('-accion_date') #BUSCAR HOW TO COMBINE QUERIES FORM DIFF MODELS
    
    filteri = request.GET.get('filteri')  # Set 'qs' as a default value
    order_by = request.GET.get('order_by')
    print(filteri)
    print(order_by)

    if order_by:
        if 'None' not in order_by:
            if order_by == 'actionr':
                qs = qs.order_by('-prospectoaccion')
            elif order_by == 'actionl':
                qs = qs.order_by('prospectoaccion')
            elif order_by == 'pub_dater':
                qs = qs.order_by('-pub_date')
            elif order_by == 'pub_datel':
                qs = qs.order_by('pub_date')
    else:
        order_by = 'None'

    if 'filteri' in request.GET:
        if not 'None' in filteri:
            qs = qs.filter(idioma__exact=filteri)
    else:
        filteri='None'

    #AQUI TENGO EL PROBLEMA QUE TENGO QUE RELACIONAR qs CON accion.
    """
    if 'accionr' in request.GET:
        qs = qs.order_by('-prospectoaccion')
        #escribir un if statement que filtre los id duplicados y solo enseñe el id de la última acción. o un for loop que solo se quede con el último item.
        # for row in qs 
              # if si el id del row se repite Ó aggarra el último row id y elimina lo demás. 
                # elimina los rows o filtralos.
    if 'accionl' in request.GET:
        qs = qs.order_by('prospectoaccion') #si remuevo values todo esta como antes. 
    
    
    
    if 'pub_dater' in request.GET:
        qs = qs.order_by('-pub_date')
        date_filter = 'pub_dater=true'
        
    if 'pub_datel' in request.GET:
        qs = qs.order_by('pub_date')
        date_filter = 'pub_datel=true'

    """
    
    
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
        "idioma_list": idiomas,
        "filteri": filteri,
        "order_by" : order_by,
    }
    
    template = 'prospectos/prospecto_list.html'
    return render(request, template, context)  
    
class ProspectoCreate(CreateView):
    model = Prospecto
    fields = '__all__'

class ProspectoUpdate(UpdateView):
    model = Prospecto
    fields = '__all__'

from django.urls import reverse

class ProspectoAccionCreate(CreateView):
    """
    Form for adding una acción. Requires login (despues poner)
    """
    model = ProspectoAccion
    fields = ['tipo_accion','descripcion',]

    def get_context_data(self, **kwargs):
        """
        Add associated prospecto to form template so can display its name in HTML.
        """
        # Call the base implementation first to get a context
        context = super(ProspectoAccionCreate, self).get_context_data(**kwargs)
        # Get the prospecto from id and add it to the context
        context['prospecto'] = get_object_or_404(Prospecto, pk = self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        """
        Add autor and associated prospecto to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as autor of comment
        form.instance.autor = self.request.user
        #Associate comment with prospecto based on passed id
        form.instance.prospecto=get_object_or_404(Prospecto, pk = self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(ProspectoAccionCreate, self).form_valid(form)

    def get_success_url(self): 
        """
        After posting comment return to associated blog.
        """
        return reverse('prospecto-detail', kwargs={'pk': self.kwargs['pk'],})

def desinteresar(request, pk):
    a = Prospecto.objects.get(id=pk) # get an article that matches that id and return it into  variable a
    status = a.status
    status = 'd'
    a.status = status #minuto 9
    a.save() #save to the model

    return HttpResponseRedirect('razon')

def reinteresar(request, pk):
    a = Prospecto.objects.get(id=pk) # get an article that matches that id and return it into  variable a
    status = a.status
    status = 'p'
    a.status = status #minuto 9
    a.save() #save to the model
    
    # redirect to the same URL:
    return HttpResponseRedirect(reverse('prospecto-detail', args=(pk,)))
    
class ProspectoRazonCreate(CreateView):
    """
    Form for adding una razón. Requires login (despues poner)
    """
    model = ProspectoRazon
    fields = ['tipo_razon', 'comentario',]

    def get_context_data(self, **kwargs):
        """
        Add associated prospecto to form template so can display its name in HTML.
        """
        # Call the base implementation first to get a context
        context = super(ProspectoRazonCreate, self).get_context_data(**kwargs)
        # Get the prospecto from id and add it to the context
        context['prospecto'] = get_object_or_404(Prospecto, pk = self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        """
        Add autor and associated prospecto to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as autor of comment
        form.instance.autor = self.request.user
        #Associate comment with prospecto based on passed id
        form.instance.prospecto=get_object_or_404(Prospecto, pk = self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(ProspectoRazonCreate, self).form_valid(form)

    def get_success_url(self): 
        """
        After posting comment return to associated blog.
        """
        return reverse('prospecto-detail', kwargs={'pk': self.kwargs['pk'],})
        
def prospecto_activo_list(request):
    query = request.GET.get('q', None)
    qs = Prospecto.objects.all().filter(status__exact='p').order_by('nombre') 
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
    template = 'prospectos/prospectos_activos_list_all.html'
    return render(request, template, context) 
    
        
def prospecto_desinteresado_list(request):
    query = request.GET.get('q', None)
    qs = Prospecto.objects.all().filter(status__exact='d').order_by('nombre') 
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
    template = 'prospectos/prospectos_desinteresados_list_all.html'
    return render(request, template, context) 
    