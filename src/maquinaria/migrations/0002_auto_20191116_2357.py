# Generated by Django 2.0.13 on 2019-11-17 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maquinaria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquinaria',
            name='fraccion_tiempo',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Precio por hora'),
        ),
    ]