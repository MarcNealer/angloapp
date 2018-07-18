from django.urls import path
from . import views


urlpatterns = [
    path('grupos/', views.grupos_list, name='grupos'),
    path('grupo/<int:pk>', views.GrupoDetailView.as_view(), name='grupo-detail'),
    path('alumnos/', views.alumnos_list, name='alumnos'),
    path('alumno/<int:pk>', views.AlumnoDetailView.as_view(), name='alumno-detail'),
    path('grupo/nuevo', views.GrupoCreate.as_view(), name='nuevo-grupo'),
    path('alumno/nuevo', views.AlumnoCreate.as_view(), name='nuevo-alumno'),
    path('alumno/<int:pk>/inscribir/', views.AlumnoUpdate.as_view(), name='inscribir-alumno'),
    path('alumno/<int:pk1>/remover-alumno/<int:pk2>', views.remover, name='remover-alumno'),
    path('alumno/<int:pk1>/remover-grupo/<int:pk2>', views.remover_grupo, name='remover-grupo'),
    path('members', views.MemberListView.as_view(), name='members'),
    path('miembro/nuevo', views.MemberCreate.as_view(), name='nuevo-miembro'),
    path('miembro/remover/<int:pk>', views.remover_miembro, name='remover-miembro'),
    path('miembro/<int:pk>/inscribir', views.inscribir, name='inscribir-miembro'),
]