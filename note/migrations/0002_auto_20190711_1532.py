# Generated by Django 2.2.3 on 2019-07-11 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='priority',
            new_name='proiority',
        ),
    ]
