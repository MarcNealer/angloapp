# Generated by Django 2.0.2 on 2018-05-23 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0020_auto_20180522_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='nombre_preinscritos',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='grupos.Preinscritos'),
        ),
    ]
