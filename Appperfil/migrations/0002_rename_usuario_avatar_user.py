# Generated by Django 4.0.3 on 2022-04-21 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appperfil', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatar',
            old_name='usuario',
            new_name='user',
        ),
    ]