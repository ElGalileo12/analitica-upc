# Generated by Django 4.2.5 on 2023-10-13 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_egreacademica_id_egresado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='egreacademica',
            name='ID_NIVEL',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='egreacademica',
            name='ID_SEGNDALENGUA',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='egrelaboral',
            name='ID_EXP_ACOMU',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='egrelaboral',
            name='ID_NOMBRE_EMPRESA',
            field=models.CharField(default=1, max_length=35),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='egrelaboral',
            name='ID_TRABAJA_NOMBRE_EMPRESA',
            field=models.CharField(default=1, max_length=35),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='egrelaboral',
            name='ID_UBICACION_EMPRESA',
            field=models.CharField(default=1, max_length=35),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='egremotivacion',
            name='ID_MOT_CARNET',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='egremotivacion',
            name='ID_MOT_SERVICIO',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='egremotivacion',
            name='ID_MOT_SERVICIO_DESEADO',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='egresados',
            name='ID_DISCAPACIDAD',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]