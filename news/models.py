from django.db import models

from datetime import datetime

class News(models.Model):
    title = models.CharField(max_length = 50, verbose_name= 'عنوان')
    body = models.TextField(verbose_name='متن')
    image_main = models.ImageField(upload_to='photos/news/%Y%m%d',blank=True, verbose_name = 'تصویر اصلی')
    image_1 = models.ImageField(upload_to='photos/news/%Y%m%d', blank=True, verbose_name = 'تصویر فرعی')
    register_time = models.DateTimeField(default= datetime.now, verbose_name='زمان ثبت خبر')
    importance = models.BooleanField(default=True,verbose_name='خبر مهم')
    status = models.BooleanField(default=True,verbose_name='وضعیت')

    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural = 'خبرها'
    def __str__(self):
        return self.title