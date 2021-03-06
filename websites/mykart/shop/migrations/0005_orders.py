# Generated by Django 2.2.3 on 2020-04-02 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200401_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(default='', max_length=70)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=70)),
                ('address', models.CharField(default='', max_length=70)),
                ('city', models.CharField(default='', max_length=70)),
                ('state', models.CharField(default='', max_length=70)),
                ('zip_code', models.CharField(default='', max_length=111)),
            ],
        ),
    ]
