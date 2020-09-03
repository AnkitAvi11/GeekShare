# Generated by Django 3.1 on 2020-09-03 14:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200903_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notification',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 3, 14, 49, 59, 697171, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='joined_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 3, 14, 49, 59, 697171, tzinfo=utc)),
        ),
    ]
