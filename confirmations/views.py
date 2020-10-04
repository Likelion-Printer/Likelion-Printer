from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from accounts import models as accounts_models
from orders import models as orders_models
from . import models
import datetime

# Create your views here.
def my_order(request):
    user_id = request.user.id
    order_user = get_object_or_404(accounts_models.User, id=user_id)
    myorder = order_user.orders.all()  # related name 사용
    return render(
        request, "my_order.html", {"myorder": myorder, "order_user": order_user}
    )


def manage_order(request):
    status = orders_models.Order.status
    manager_printer = request.user.my_printer
    print_pending = orders_models.Order.objects.filter(printer_house =manager_printer ,status="pending")
    print_complete = orders_models.Order.objects.filter(printer_house =manager_printer ,status="complete")
    
    return render(
        request,
        "manager.html",
        {"print_pending": print_pending, "print_complete": print_complete,"manager_printer":manager_printer},
    )


def complete(request, id):
    order = orders_models.Order.objects.filter(id=id)
    order.update(status="complete")
    return redirect("manage_order")


def take_back(reqeust, id):
    order = orders_models.Order.objects.filter(id=id)
    order.update(status="pending")
    return redirect("manage_order")


def manage_stats(request):
    if request.user.is_manager == True:
        today = datetime.date.today()
        this_year = today.year
        this_month = today.month
        total_sum = 0

        # house = models.Printer_house.objects.filter(id= request.user.my_printer.id)
        for order in orders_models.Order.objects.filter(
            order_time__month=this_month, 
        printer_house =request.user.my_printer ):
            total_sum += order.cost()
        return render(request, "manager_stats.html",{"total_income":total_sum})
    else:
        raise Http404("접근할 수 없는 페이지입니다.")