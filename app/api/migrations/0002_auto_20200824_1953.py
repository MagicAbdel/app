# Generated by Django 3.1 on 2020-08-24 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='added_by',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='created_date',
        ),
    ]
