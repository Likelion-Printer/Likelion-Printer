from django.db import models

# Create your models here.
class Order(models.Model):
    cost = models.IntegerField()
    is_canceled = models.BooleanField(default=False)