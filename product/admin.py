from django.contrib import admin
from .models import *

@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Delivery)

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('title','cost',)

@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','sub_title','price', 'maintenance','status')

@admin.register(Order)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer','register_time','status','delivery',)
    list_editable = ('delivery',)