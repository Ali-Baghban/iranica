# Generated by Django 3.0.3 on 2020-03-04 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20200228_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products_type_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='تعداد انواع محصول'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.BooleanField(choices=[(1, 'پرداخت شده'), (0, 'پرداخت نشده')], default=0, verbose_name='وضعیت پرداخت'),
        ),
    ]
