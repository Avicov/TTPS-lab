# Generated by Django 3.2.8 on 2021-12-12 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_paciente_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='dni',
            field=models.BigIntegerField(unique=True),
        ),
    ]
