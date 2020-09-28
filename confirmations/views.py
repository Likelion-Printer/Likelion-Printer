from django.shortcuts import render, get_object_or_404, redirect
from accounts import models as accounts_models
from orders import models as orders_models

# Create your views here.
def my_order(request):
    user_id = request.user.id
    order_user = get_object_or_404(accounts_models.User, id=user_id)
    myorder = order_user.orders.all()  # related name 사용
    return render(
        request, "my_order.html", {"myorder": myorder, "order_user": order_user}
    )


def manage_order(request):
    printer_orders = orders_models.Order.objects.all()
    status = orders_models.Order.status
    print_pending = orders_models.Order.objects.filter(status="pending")
    print_complete = orders_models.Order.objects.filter(status="complete")
    return render(
        request,
        "manager.html",
        {"print_pending": print_pending, "print_complete": print_complete,},
    )


def complete(request, id):
    order = orders_models.Order.objects.filter(id=id)
    order.update(status="complete")
    return redirect("manage_order")


def take_back(reqeust, id):
    order = orders_models.Order.objects.filter(id=id)
    order.update(status="pending")
    return redirect("manage_order")
