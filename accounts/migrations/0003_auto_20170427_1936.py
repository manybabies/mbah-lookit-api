# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 19:36
from __future__ import unicode_literals

from django.db import migrations
import project.fields.datetime_aware_jsonfield


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user__identicon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demographicdata',
            name='extra',
            field=project.fields.datetime_aware_jsonfield.DateTimeAwareJSONField(blank=True),
        ),
    ]