# Generated by Django 2.0.2 on 2018-05-23 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0021_auto_20180522_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='gpreinscrito',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='grupos.Preinscritos'),
        ),
    ]
