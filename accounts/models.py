from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import auth

# Create your models here.
class User(AbstractUser):
    order_time = models.DateTimeField(auto_now_add = True)
    pickup_time = models.DateTimeField()
    current_balance = models.DecimalField(max_digits = 15, decimal_places= 6)
