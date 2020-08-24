# Generated by Django 3.1 on 2020-08-24 19:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200824_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='lastname',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('[a-zA-Z0-9]')]),
        ),
        migrations.AlterField(
            model_name='child',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('[a-zA-Z0-9]')]),
        ),
    ]
