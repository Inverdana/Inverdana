# Generated by Django 2.2.5 on 2019-11-26 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0037_auto_20191126_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='final_date',
            field=models.DateTimeField(verbose_name='Fecha Final'),
        ),
        migrations.AlterField(
            model_name='event',
            name='info',
            field=models.TextField(max_length=900, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='event',
            name='initial_date',
            field=models.DateTimeField(verbose_name='Fecha Inicial'),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='event',
            name='size',
            field=models.IntegerField(default=0, verbose_name='Cantidad de Asistentes'),
        ),
    ]