from django.db import models
import datetime
from orders.models import Order

# Create your models here.
class Printer_house(models.Model):

    house_name = models.CharField(max_length=200)
    phone_nubmer = models.CharField(max_length=13)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.house_name

    def total_income(self):
        # now = datetime.datetime.now()
        # last_month = now - datetime.timedelta(weeks=4)
        # now_date = now.strftime("%Y-%M-%D")
        # last_month_date = last_month.strftime("%Y-%M-%D")
        temp_sum = 0
        # temp = orders_models.objects.filter(date__range=["last_month_date", "now_date"])
        for order in Order.objects.all():
            temp_sum += order.cost()
        return temp_sum

