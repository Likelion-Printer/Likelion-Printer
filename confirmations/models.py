from django.db import models
from orders import Order

# Create your models here.
class Printer_house(models.Model):
    house_name = CharField(max_length=200, default="-")

