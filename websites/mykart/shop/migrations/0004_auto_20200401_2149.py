# Generated by Django 2.2.3 on 2020-04-01 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='price',
            new_name='phone',
        ),
    ]
