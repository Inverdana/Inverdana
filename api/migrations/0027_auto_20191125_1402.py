# Generated by Django 2.2.5 on 2019-11-25 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_post_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user_id',
            new_name='username',
        ),
    ]
