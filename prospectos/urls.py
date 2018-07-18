from django.urls import path
from . import views

urlpatterns = [
    path('prospecto/<int:pk>', views.ProspectoDetailView.as_view(), name='prospecto-detail'),
    path('prospectos/', views.prospecto_list_view, name='prospectos'),
    path('prospecto/agregar', views.ProspectoCreate.as_view(), name='agregar-prospecto'),
    path('prospecto/<int:pk>/editar/', views.ProspectoUpdate.as_view(), name='editar-prospecto'),
    path('prospecto/<int:pk>/accion/', views.ProspectoAccionCreate.as_view(), name='prospecto_accion'),
    path('prospecto/<int:pk>/desinteresar', views.desinteresar, name='prospecto-desinteresar'),
    path('prospecto/<int:pk>/razon/', views.ProspectoRazonCreate.as_view(), name='prospecto_razon'),
    path('prospecto/<int:pk>/reinteresar', views.reinteresar, name='prospecto-reinteresar'),
    path('activos/', views.prospecto_activo_list, name='prospectos-activos'),
    path('desinteresados/', views.prospecto_desinteresado_list, name='prospectos-desinteresados'),
    path('prospectos/idiomas', views.IdiomaListView.as_view(), name='prospectos-idiomas'),
]
