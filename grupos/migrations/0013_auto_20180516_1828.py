# Generated by Django 2.0.2 on 2018-05-16 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0012_alumno_grupo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('i', 'Inscrito'), ('p', 'Pre-inscrito')], default='p', help_text='Status del prospecto', max_length=1)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos.Alumno')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos.Grupo')),
            ],
        ),
        migrations.AddField(
            model_name='grupo',
            name='members',
            field=models.ManyToManyField(related_name='preubanormal', through='grupos.Membership', to='grupos.Alumno'),
        ),
    ]