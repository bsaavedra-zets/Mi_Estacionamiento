# Generated by Django 3.2.3 on 2021-06-17 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=100, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=254)),
                ('type_request', models.IntegerField(choices=[[0, 'Consulta'], [1, 'Sugerencia'], [2, 'Reclamo']], verbose_name='Tipo de Solicitud')),
                ('message', models.TextField(verbose_name='Mensaje')),
            ],
        ),
    ]
