# Generated by Django 2.0.2 on 2018-03-23 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prospectos', '0005_prospectoaccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ingresa los tipos de acción', max_length=100)),
            ],
        ),
    ]
