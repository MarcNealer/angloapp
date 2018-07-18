# Generated by Django 2.0.2 on 2018-05-16 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0007_auto_20180402_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('i', 'Inscrito'), ('p', 'Pre-inscrito')], default='p', help_text='Status del prospecto', max_length=1)),
            ],
        ),
        migrations.RenameField(
            model_name='alumno',
            old_name='grupo',
            new_name='members',
        ),
        migrations.AddField(
            model_name='membership',
            name='alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos.Alumno'),
        ),
        migrations.AddField(
            model_name='membership',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos.Grupo'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='members',
            field=models.ManyToManyField(through='grupos.Membership', to='grupos.Alumno'),
        ),
    ]