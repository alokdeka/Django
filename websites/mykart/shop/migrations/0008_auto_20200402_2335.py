# Generated by Django 2.2.3 on 2020-04-02 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20200402_2258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='items_json',
            new_name='itemsJson',
        ),
    ]
