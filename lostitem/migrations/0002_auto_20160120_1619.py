# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-20 15:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lostitem', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ItemClass',
            new_name='ItemLost',
        ),
    ]