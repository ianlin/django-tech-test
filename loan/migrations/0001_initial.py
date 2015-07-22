# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('registered_number', models.CharField(max_length=8)),
                ('business_sector', models.CharField(max_length=4, choices=[(b'RE', b'retail'), (b'PS', b'Profession Services'), (b'FOOD', b'Food and Drink'), (b'ENT', b'Entertainment')])),
                ('owner', models.ForeignKey(to='loan.Borrower')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(100000)])),
                ('days', models.PositiveIntegerField()),
                ('reason', models.TextField()),
                ('business', models.ForeignKey(to='loan.Business')),
            ],
        ),
    ]
