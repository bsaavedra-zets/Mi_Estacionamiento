# Generated by Django 3.2.3 on 2021-06-28 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='especificacion',
        ),
    ]
