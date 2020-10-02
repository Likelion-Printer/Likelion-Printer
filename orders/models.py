from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import timedelta, timezone, datetime
# from subprocess import check_output

# Create your models here.

class Order(models.Model):
    is_canceled = models.BooleanField(default=False)
    is_in_process = models.BooleanField(default=True)
    customer = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="orders"
    )
    printer_house = models.ForeignKey(
        "confirmations.Printer_house",
        on_delete=models.CASCADE,
        related_name="orders",
        null=True,
    )

    order_time = models.DateTimeField(auto_now=True)
    pickup_time = models.DateTimeField(null=True)

    STATUS = (
        ("picked_up", "픽업완료"),
        ("complete", "인쇄완료"),
        ("pending", "주문대기"),
    )
    status = models.CharField(max_length=200, choices=STATUS, default="pending")

    OPTION_COLOR = (("black", "흑백"), ("color", "칼라"))
    OPTION_PRINT = (("single", "단면"), ("double", "양면"))
    OPTION_PAGES = (("four", "4개"), ("two", "2개"), ("one", "1개"))
    OPTION_DIRECTIONS = (("horizontal", "가로"), ("vertical", "세로"))
    OPTION_FLIP = (("horizontal", "옆으로 넘김"), ("vertical", "위로 넘김"))

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
    options_directions = models.CharField(
        max_length=200, choices=OPTION_DIRECTIONS, default="vertical"
    )
    options_flip = models.CharField(
        max_length=200, choices=OPTION_FLIP, default="horizontal"
    )
    comments = models.TextField()

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

    # def set_time(self):
    #     now = timezone.localtime(timezone.now())
    #     self.order_time = now

class File(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_file = models.FileField(upload_to="doc/%Y/%m/%d/")
    name = models.CharField(max_length=200)
    size = models.FloatField()
    # num_of_pages = models.IntegerField()

    # def set_num_pages(self, pdf_path):
    #     output = check_output(["pdfinfo", pdf_path]).decode()
    #     pages_line = [line for line in output.splitlines() if "Pages:" in line][0]
    #     num_pages = int(pages_line.split(":")[1])
    #     self.num_of_pages = num_pages
    

