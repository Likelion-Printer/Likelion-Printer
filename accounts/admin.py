from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin 

# Register your models here.



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
        list_display = [
            'username',
        'order_time',
        'pickup_time',
        'current_balance',]

        fieldsets = UserAdmin.fieldsets + (
            ('order_info', 
            {'fields': 
            (        
            'order_time',
            'pickup_time',
            'current_balance',)
            }
            ) ,
        )
        readonly_fields = ('order_time','current_balance' )
        
        add_fieldsets = UserAdmin.add_fieldsets + (
            (None, {'fields': ('custom_field',)}),
        )

