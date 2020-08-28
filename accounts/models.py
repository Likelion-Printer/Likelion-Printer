from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import models as django_models
import datetime

# Create your models here.
class User(AbstractUser):
    order_time = models.DateTimeField(auto_now = True)
    pickup_time = models.DateTimeField(auto_now = False, default = datetime.datetime.now())
    current_balance = models.DecimalField(max_digits = 15, decimal_places= 2, default = 0)

    def __str__(self):
        return self.username
