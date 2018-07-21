from .models import Grupo, Membership


def migrate_grupo(old_group, new_group):
    recs = Membership.objects.filter(grupo=old_group)
    new_grupo = Grupo.objects.get(id=new_group)
    for item in recs.iterator():
        new_rec = item
        new_rec.pk = None
        new_rec.grupo = new_grupo
        new_rec.save()




