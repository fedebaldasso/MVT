# Generated by Django 4.1.3 on 2022-12-06 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppMVT', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familiar',
            name='fecha_nacimiento',
        ),
    ]
