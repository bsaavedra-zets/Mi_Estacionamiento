# Generated by Django 3.2.3 on 2021-06-30 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0005_address_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='value',
            field=models.IntegerField(default=0, verbose_name='Valor Estacionamiento'),
        ),
    ]
