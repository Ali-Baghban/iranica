# Generated by Django 3.0.3 on 2020-02-08 06:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200208_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='register_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='زمان ثبت خبر'),
        ),
    ]
