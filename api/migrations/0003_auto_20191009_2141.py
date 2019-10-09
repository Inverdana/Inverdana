# Generated by Django 2.2.5 on 2019-10-09 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190930_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='share',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shares', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tree',
            name='shareholders',
            field=models.ManyToManyField(through='api.Share', to=settings.AUTH_USER_MODEL),
        ),
    ]