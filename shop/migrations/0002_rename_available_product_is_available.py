# Generated by Django 3.2.5 on 2021-07-21 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='available',
            new_name='is_available',
        ),
    ]
