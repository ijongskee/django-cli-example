# Generated by Django 2.0.3 on 2018-06-14 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cli_example', '0002_auto_20180613_1656'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Residence',
            new_name='Resident',
        ),
        migrations.RenameField(
            model_name='resident',
            old_name='residence_date_created',
            new_name='resident_date_created',
        ),
    ]
