# Generated by Django 4.0.3 on 2022-03-06 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.RenameModel(
            old_name='Ships',
            new_name='Ship',
        ),
    ]
