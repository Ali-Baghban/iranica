from datetime import datetime

from django.db import models
from accounts.models import *

class Delivery(models.Model):
    title = models.CharField(max_length=50, verbose_name='شرکت ارسال کننده')
    cost = models.IntegerField(verbose_name='هزینه ارسال')
    STATUS_CHOICES = (
        (1,'در دسترس'),
        (0,'خارج ازدسترس')
    )
    status = models.BooleanField(choices=STATUS_CHOICES,default=1, verbose_name='وضعیت سرویس')
    class Meta:
        verbose_name = 'شرکت ارسال کننده '
        verbose_name_plural = 'شرکت های ارسال کننده '
    
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
    
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان' , blank=True)
    sub_title = models.CharField(max_length=50, verbose_name='زیر عنوان', blank=True)
    category = models.ForeignKey("category", verbose_name='دسته بندی', on_delete=models.CASCADE)
    caption = models.TextField(verbose_name = 'توضیحات')
    price = models.CharField(max_length=20, verbose_name = 'قیمت')
    maintenance = models.IntegerField(default= 1000, verbose_name= 'موجودی محصول')
    register_time = models.DateTimeField(default= datetime.now, verbose_name='زمان ثبت کالا')
    STATUS_CHOICES = (
        (1,'موجود'),
        (0,'ناموجود')
    )
    status = models.BooleanField(choices = STATUS_CHOICES, default=1, verbose_name= 'وضعیت محصول')
    STATUS_CHOICES = (
        (0,'ندارد'),
        (1,'دارد')
    )
    offer = models.BooleanField(default=False, verbose_name= 'تخفیف محصول')
    discount = models.CharField(max_length=20, verbose_name = 'درصد تخقیف محصول' ,default='0')
    image_main = models.ImageField(upload_to='photos/product/%Y%m%d',blank=True, verbose_name='تصویر اصلی')
    image_1 = models.ImageField(upload_to='photos/product/%Y%m%d',blank=True, verbose_name='تصویر اول')
    image_2 = models.ImageField(upload_to='photos/product/%Y%m%d',blank=True, verbose_name='تصویر دوم')
    image_3 = models.ImageField(upload_to='photos/product/%Y%m%d',blank=True, verbose_name='تصویر سوم')
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
    
    def __str__(self):
        return self.title


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE ,verbose_name='مشتری',)
    products_ordered = models.TextField(verbose_name='سفارشات مشتری', blank=True)
    products_type_count = models.IntegerField(verbose_name='تعداد انواع محصول',blank=True,null=True)
    address = models.TextField(verbose_name='آدرس', blank=True)
    details = models.TextField(verbose_name='توضیحات', blank=True)
    total_cost = models.CharField(max_length=20, verbose_name='جمع سفارش',null=True)
    register_time = models.DateTimeField(default=datetime.now, verbose_name='زمان ثبت کالا')
    STATUS_CHOICES = (
        (1, 'پرداخت شده'),
        (0, 'پرداخت نشده')
    )
    status = models.BooleanField(choices=STATUS_CHOICES, default=0, verbose_name='وضعیت پرداخت')
    STATUS_CHOICES = (
        (0, 'تحویل نشده'),
        (1, 'تحویل شده')
    )
    bill_id = models.CharField(max_length=100, verbose_name='شماره رسید', blank=True)
    deliver_with = models.ForeignKey(Delivery, verbose_name='شرکت تحویل دهنده', on_delete=models.CASCADE, null=True,)
    delivery = models.BooleanField(choices=STATUS_CHOICES, default=0, verbose_name='وضعیت تحویل به پست')
    post_id = models.CharField(max_length=100, verbose_name='کد رهگیری مرسوله', blank=True)
    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'

    def __str__(self):
        return str(self.customer)