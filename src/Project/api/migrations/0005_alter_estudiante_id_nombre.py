# Generated by Django 4.2.4 on 2023-08-28 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_estudiante_id_sisben'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='ID_NOMBRE',
            field=models.CharField(max_length=50),
        ),
    ]
