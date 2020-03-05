from django.urls import path
from .views import index, rules
urlpatterns = [
    path('', index, name='index' ),
    path('rules', rules, name='rules')

]
