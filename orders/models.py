from django.db import models
from accounts import User
from confirmations import Printer_house
from datetime import timedelta, timezone

# Create your models here.
class Order(models.Model):
    
    customer = models.ForeignKey(User, related_name='orders', null=True, blank=True)
    printer_house = models.ForeignKey(Printer_house, related_name='orders', null=True, blank=True)
    order_time = models.DateTimeField(auto_now = True)
    pickup_time = models.DateTimeField(auto_now = False, default = datetime.datetime.now() +timedelta(seconds=3600))
    is_canceled = models.BooleanField(default=False)
    cost = models.IntegerField()
    # files = models.

    STATUS = (("confirmed", "주문확인"),
        ("complete", "인쇄완료"),
        ("pending", "주문대기"),
    status = models.CharField(max_length=200, choices = STATUS, default = STATUS_PENDING)

    OPTION_COLOR = (("black", "흑백"),
    ("color", "칼라"))
    OPTION_PRINT = (("single", "단면"), ("double", "양면"))
    OPTION_PAGES = (
        ("four", "4개"),("two", "2개"), ("one", "1개")
    )
    options_color = models.CharField(max_length=200, choices = OPTION_COLOR, default = "black")
    options_print = models.CharField(max_length=200, choices = OPTION_PRINT, default = "double")
    options_pages = models.CharField(max_length=200, choices = OPTION_PAGES, default = "four")


