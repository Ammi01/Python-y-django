# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 15:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Boletin', '0003_remove_habitaciones_disponible'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='DNI',
            new_name='dni',
        ),
    ]