# Generated by Django 3.0.3 on 2020-02-25 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200225_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.CharField(blank=True, max_length=20, verbose_name='درصد تخقیف محصول'),
        ),
    ]
