# Generated by Django 4.2.5 on 2023-09-23 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_egresados_egreacademica_egrelaboral_egremotivacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='egresados',
            name='ID_prueba',
        ),
    ]
