# Generated by Django 3.2.3 on 2021-06-29 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210629_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='available',
        ),
        migrations.AddField(
            model_name='client',
            name='avaible',
            field=models.BooleanField(null=True, verbose_name='Disponible'),
        ),
        migrations.AlterField(
            model_name='client',
            name='car_year',
            field=models.DateTimeField(),
        ),
    ]
