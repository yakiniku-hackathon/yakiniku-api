# Generated by Django 5.0 on 2024-06-21 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mystery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mystery',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='mystery_id',
            new_name='mystery',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='user_id',
            new_name='user',
        ),
    ]
