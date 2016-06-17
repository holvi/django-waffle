# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('waffle', '0001_initial'),
        (settings.CUSTOM_USER_MODEL.split('.')[0], '__latest__')
    ]

    operations = [
        migrations.AlterField(
            model_name='flag',
            name='users',
            field=models.ManyToManyField(help_text='Activate this flag for these users.', to=settings.CUSTOM_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
