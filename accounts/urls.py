from django.urls import path
from .views import *
urlpatterns = [
     path('', dashboard_view , name='dashboard'),
     path('order_details/<int:order_id>', order_details , name='order_details'),
     path('edit_profile', dashboard_profile_edit, name='edit_profile'),
     path('login', dashboard_login, name='login'),
     path('logout', dashboard_logout, name='logout'),
     path('register', dashboard_register, name='register'),
     path('card', card_view , name='card'),
     path('card_remove/<int:item_id_remove>', card_remove , name='card_remove'),
]
