# Generated by Django 2.0.2 on 2018-05-20 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0013_auto_20180516_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, related_name='preubanormal', through='grupos.Membership', to='grupos.Alumno'),
        ),
    ]