from .models import History

def history_add(grupo, alumno, status):
    History.objects.create(nombre=grupo.nombre,
                           fecha_inicio=grupo.fecha_inicio,
                           idioma=grupo.idioma,
                           nivel=grupo.nivel,
                           horario=grupo.horario,
                           profesor=grupo.profesor,
                           salon=grupo.salon,
                           alumno=alumno,
                           status=status)
    return