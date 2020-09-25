from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "order_num",
        "customer",
        "pickup_time",
        "order_time",
        "status",
        "number_of_pages",
        "options_color",
        "options_print",
        "options_pages",
        "cost",
    )
    readonly_fields = ("cost",)

    list_filter = ("order_time", "pickup_time")

    list_display_links = ['order_num', 'customer']
