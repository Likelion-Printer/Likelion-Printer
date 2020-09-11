from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "customer",
        "order_time",
        "pickup_time",
        "status",
        "number_of_pages",
        "options_color",
        "options_print",
        "options_pages",
        "cost",
        "order_num",
    )
    readonly_fields = ("cost",)

    list_filter = ("order_time", "pickup_time")

