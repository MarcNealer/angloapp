# Generated by Django 2.0.2 on 2018-05-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0017_auto_20180520_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='nombre_preinscritos',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
