# Generated by Django 2.0.5 on 2018-06-14 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cli_example', '0003_auto_20180614_1846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='baranggay',
            old_name='baranggay_date_created',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='baranggay',
            old_name='baranggay',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='city',
            old_name='city',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='resident',
            old_name='resident_date_created',
            new_name='date_created',
        ),
    ]
