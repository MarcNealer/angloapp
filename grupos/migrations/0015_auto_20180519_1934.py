# Generated by Django 2.0.2 on 2018-05-20 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0014_auto_20180519_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='members',
            field=models.ManyToManyField(related_name='preubanormal', through='grupos.Membership', to='grupos.Alumno'),
        ),
    ]
