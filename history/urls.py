from django.urls import path
from . import views


urlpatterns = [
    path('select/', views.historyselect, name='history-select'),
    path('grupo/', views.historygrupo, name='grupo-history'),
    path('alumno/', views.historyalumno, name='alumno-history'),
    path('all/', views.historyall, name='alumno-all'),
]