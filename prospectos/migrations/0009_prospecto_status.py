# Generated by Django 2.0.2 on 2018-03-23 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prospectos', '0008_prospectoaccion_tipo_accion'),
    ]

    operations = [
        migrations.AddField(
            model_name='prospecto',
            name='status',
            field=models.CharField(blank=True, choices=[('p', 'Prospecto Activo'), ('d', 'Desinteresado')], default='p', help_text='Status del prospecto', max_length=1),
        ),
    ]