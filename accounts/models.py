from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import models as django_models
from confirmations import Printer_house
import datetime

# Create your models here.
class User(AbstractUser):
    my_printer = models.ManyToManyField(Printer_house)
    recent_printer = models.ManyToManyField(Printer_house)
    current_balance = models.DecimalField(max_digits=15, decimal_places=1, default=0)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.username

