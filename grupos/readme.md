# changes

## utils.migrate_grupo

Pass this function the current grupo instance and the new grupo instance and it will
create new memebership records for the said new group, i.e migrate the pupil records to
the new grupo.

I have assued here that the new grupo will be created first as this might have
different details from the old one

'''
from grupos.utils import migrate_grupo

old_grupo = Grupo.objects.get(id=pk1)
new_grupo = Grupo.objects.get(id=pk2)
migrate_grupo(old_grupo, new_grupo)
'''
