from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Printer_house)
class Printer_house(admin.ModelAdmin):
    list_display = [
        "house_name",
        "phone_number",
        "address",
    ]
