# Generated by Django 4.0.3 on 2022-04-23 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('autor', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('mensaje', models.CharField(max_length=1000)),
            ],
        ),
    ]
