# Generated by Django 2.1.3 on 2018-11-09 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todu',
            old_name='creart_time',
            new_name='create_time',
        ),
        migrations.RenameField(
            model_name='todu',
            old_name='morese',
            new_name='status',
        ),
    ]
