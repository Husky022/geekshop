# Generated by Django 3.1.7 on 2021-03-25 15:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20210325_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 27, 15, 49, 32, 865082, tzinfo=utc)),
        ),
    ]
