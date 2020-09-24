from django.contrib import admin
<<<<<<< HEAD


# Register your models here.
=======
from . import models


# Register your models here.
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "customer",
        "pickup_time",
        "order_time",
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

>>>>>>> 0ad93b7b864c516fd5a1ea7f3ad6b0851aaf7bb3
