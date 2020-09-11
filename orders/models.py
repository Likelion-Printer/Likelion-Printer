from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import timedelta, timezone, datetime


# Create your models here.
class Order(models.Model):
    is_canceled = models.BooleanField(default=False)
    customer = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="orders"
    )
    printer_house = models.ForeignKey(
        "confirmations.Printer_house", on_delete=models.CASCADE, related_name="orders",
    )

    order_time = models.DateTimeField(auto_now=True)
    pickup_time = models.DateTimeField(
        auto_now=False, default=datetime.now() + timedelta(seconds=3600)
    )

    STATUS = (
        ("confirmed", "주문확인"),
        ("complete", "인쇄완료"),
        ("pending", "주문대기"),
    )
    status = models.CharField(max_length=200, choices=STATUS, default="pending")

    OPTION_COLOR = (("black", "흑백"), ("color", "칼라"))
    OPTION_PRINT = (("single", "단면"), ("double", "양면"))
    OPTION_PAGES = (("four", "4개"), ("two", "2개"), ("one", "1개"))
    options_color = models.CharField(
        max_length=200, choices=OPTION_COLOR, default="black"
    )
    options_print = models.CharField(
        max_length=200, choices=OPTION_PRINT, default="double"
    )
    options_pages = models.CharField(
        max_length=200, choices=OPTION_PAGES, default="four"
    )
    number_of_pages = models.IntegerField(
        default=1, validators=[MaxValueValidator(70), MinValueValidator(1)]
    )

    def __str__(self):
        return f"{self.customer.username}-{self.pickup_time}"

    def cost(self):
        if self.options_color == "black":
            return 50 * self.number_of_pages
        else:
            return 100 * self.number_of_pages

    def order_num(self):
        now = datetime.now()
        now_date = now.strftime("%Y%m%d")
        return now_date + str(self.id)

