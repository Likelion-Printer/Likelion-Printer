from django.db import models
import datetime
from orders.models import Order

# Create your models here.
class Printer_house(models.Model):

    house_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.house_name


