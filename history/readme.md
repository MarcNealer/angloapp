# History Module

This module is used to recorc changes to the Groups or Grupos.

## history_add

To add a record to the History, history.utils.history_add . This function acts like
an interface into the History module.

*You should not directly add records to the history model.*

While you can do this. its highly recommeded that you use the history_add interface function
for useability and reduction in coupling

To use history_add, pass a Gupo instance, Alumno instance, and a string representing details of the status change.

Example
'''
from history.utils import history_add

grupo = Gupo.objects.get(id=1)
alumno = Alumno.objects.get(id=1)

history_add(grupo, alumno, "Dropped")'''

## URLS

History has only three Urls

history/select/ brings up the select page

history/grupo/?gupo=****  displays history records for a given gupo name, where **** = the name

history/alumno/?alumno=** displays history records for an alumno, where ** is the id number of the record


# my contact details

email: marcnealer@gmail.com or marc@willowtreesoftware.com

skype: marc.stephen.nealer

hangouts marcnealer@gmail.com
