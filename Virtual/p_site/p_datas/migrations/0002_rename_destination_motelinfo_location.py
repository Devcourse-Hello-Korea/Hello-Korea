# Generated by Django 5.0.4 on 2024-04-13 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_datas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='motelinfo',
            old_name='destination',
            new_name='location',
        ),
    ]
