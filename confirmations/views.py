from django.shortcuts import render, get_object_or_404
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
