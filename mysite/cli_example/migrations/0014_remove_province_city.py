# Generated by Django 2.1.3 on 2018-11-30 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cli_example', '0013_country_island'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='province',
            name='city',
        ),
    ]
