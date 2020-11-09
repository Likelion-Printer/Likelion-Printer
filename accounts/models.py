from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=100, default="-")
    current_balance = models.IntegerField(default=0)
    my_printer = models.ForeignKey(
        "confirmations.Printer_house", on_delete=models.CASCADE, null=True
    )
    is_manager = models.BooleanField(default = False)

    def __str__(self):
        return self.username
