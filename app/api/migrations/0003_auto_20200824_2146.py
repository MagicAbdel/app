# Generated by Django 3.1 on 2020-08-24 19:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200824_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='city',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('[a-zA-Z]')]),
        ),
        migrations.AlterField(
            model_name='parent',
            name='lastname',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('[a-zA-Z]')]),
        ),
        migrations.AlterField(
            model_name='parent',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('[a-zA-Z]')]),
        ),
        migrations.AlterField(
            model_name='parent',
            name='state',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('[a-zA-Z]')]),
        ),
        migrations.AlterField(
            model_name='parent',
            name='street',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('[a-zA-Z0-9]')]),
        ),
        migrations.AlterField(
            model_name='parent',
            name='zipcode',
            field=models.IntegerField(validators=[django.core.validators.MaxLengthValidator(5), django.core.validators.MinLengthValidator(5)]),
        ),
    ]
