# Generated by Django 2.2.5 on 2019-11-05 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20191105_0655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='share',
            old_name='tree_id',
            new_name='tree',
        ),
    ]