# Generated by Django 4.2.1 on 2023-06-06 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_passangers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Passangers',
            new_name='Passanger',
        ),
    ]
