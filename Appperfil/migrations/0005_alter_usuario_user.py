# Generated by Django 4.0.3 on 2022-04-24 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Appperfil', '0004_alter_usuario_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
