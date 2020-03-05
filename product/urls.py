from django.urls import path
from .views import *

urlpatterns = [
    path('', product_view , name='products'),
    path('<int:product_id>', product_details, name='product_details'),
    path('order',order, name='order'),
    path('verify/<bill_id>/',verify, name='verify'),
]
