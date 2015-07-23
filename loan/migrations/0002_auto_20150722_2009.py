# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='business_sector',
            field=models.CharField(max_length=4, choices=[(b'RE', b'Retail'), (b'PS', b'Profession Services'), (b'FOOD', b'Food and Drink'), (b'ENT', b'Entertainment')]),
        ),
    ]
