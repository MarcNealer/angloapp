# Generated by Django 2.0.2 on 2018-05-20 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0015_auto_20180519_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='grupo',
        ),
    ]
