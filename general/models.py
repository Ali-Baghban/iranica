from django.db import models

class Settings(models.Model):
    site_title = models.CharField(max_length=50, verbose_name= 'عنوان سایت', blank = False, default='فروشگاه')
    phone = models.CharField(max_length=15, verbose_name = 'شماره همراه', blank = True)
    tel = models.CharField(max_length=15, verbose_name = 'شماره ثابت', blank = True)
    telgram = models.CharField(max_length=25, verbose_name = 'Telegram ID', blank = True)
    instagram = models.CharField(max_length=25, verbose_name = 'Instagram ID', blank = True)
    email = models.EmailField(max_length=35, verbose_name = 'ایمیل',blank = True)
    logo = models.ImageField(upload_to='photos/logo/%Y%m%d',blank=True)
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('deactive','Deactive')
    )
    status = models.CharField(max_length = 10 , choices = STATUS_CHOICES , default = 'active')
    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.site_title
    
class Rules(models.Model):
    title = models.CharField(max_length=50,blank=False, default='قوانین سایت', verbose_name='عنوان')
    caption = models.TextField(blank=True, verbose_name='متن قوانین')
    image_main = models.ImageField(upload_to='photos/rules/%Y%m%d', verbose_name='تصویر')

    class Meta:
        verbose_name = 'قانون'
        verbose_name_plural = 'قوانین'
    def __str__(self):
        return self.title
    
    
