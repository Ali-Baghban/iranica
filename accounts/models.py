from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=15,blank=True)