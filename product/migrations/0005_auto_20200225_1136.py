# Generated by Django 3.0.3 on 2020-02-25 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200225_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='offer',
            field=models.BooleanField(default=False, verbose_name='تخفیف محصول'),
        ),
    ]
