# Generated by Django 3.0.3 on 2020-02-08 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200208_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='importance',
            field=models.BooleanField(default=True, verbose_name='خبر مهم'),
        ),
    ]