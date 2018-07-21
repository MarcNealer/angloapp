from history.utils import history_add

def save_history(sender, instance, **kwargs):
    if kwargs['created']:
        history_add(instance.grupo, instance.alumno,
                    "New Membership. Status: {}".format(instance.status))
    else:
        history_add(instance.grupo, instance.alumno,
                    "Membership updated. Status: {}".format(instance.status))