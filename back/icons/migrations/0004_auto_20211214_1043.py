# Generated by Django 3.2.9 on 2021-12-14 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icons', '0003_alter_icon_bots'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='icon',
            name='bots',
        ),
        migrations.RemoveField(
            model_name='icon',
            name='shrooms',
        ),
    ]
