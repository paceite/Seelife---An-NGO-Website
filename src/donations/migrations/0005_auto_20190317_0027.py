# Generated by Django 2.1.7 on 2019-03-17 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0004_auto_20190316_2218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='donation',
            options={'ordering': ['-timestamp']},
        ),
    ]
