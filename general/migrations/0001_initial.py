# Generated by Django 3.0.3 on 2020-02-07 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='قوانین سایت', max_length=50, verbose_name='عنوان')),
                ('caption', models.TextField(blank=True, verbose_name='متن قوانین')),
                ('image_main', models.ImageField(upload_to='photos/rules/%Y%m%d', verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'قانون',
                'verbose_name_plural': 'قوانین',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(default='فروشگاه', max_length=50, verbose_name='عنوان سایت')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='شماره همراه')),
                ('tel', models.CharField(blank=True, max_length=15, verbose_name='شماره ثابت')),
                ('telgram', models.CharField(blank=True, max_length=25, verbose_name='Telegram ID')),
                ('instagram', models.CharField(blank=True, max_length=25, verbose_name='Instagram ID')),
                ('email', models.EmailField(blank=True, max_length=35, verbose_name='ایمیل')),
                ('logo', models.ImageField(blank=True, upload_to='photos/logo/%Y%m%d')),
                ('status', models.CharField(choices=[('active', 'Active'), ('deactive', 'Deactive')], default='active', max_length=10)),
            ],
            options={
                'verbose_name': 'تنظیمات',
                'verbose_name_plural': 'تنظیمات',
            },
        ),
    ]
