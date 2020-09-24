from django.shortcuts import render, redirect
from . models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def step1(request):
    if not(request.user.is_authenticated):
        return redirect('home')

    return render(request, 'step1.html')

def create_order(request):
    order = Order(printer_house_id = 1)
    order.customer = request.user
    # order.printer_house = Printer_house.objects.get(id = 1)
    order.options_color = "color"
    order.options_print = "single"
    order.options_pages = "two"
    order.number_of_pages = 5
    order.cost()
    order.order_num()
    order.save()
    id = order.pk
    return redirect('step2' , id)

def step2(request, id):
    order = Order.objects.get(id=id)
    return render(request, 'step2.html', { 'order' : order })

def payment(request, id):
    order = Order.objects.get(id=id)
    return render(request, 'payment.html', { 'order' : order })

def order_result(request, id):
    order = Order.objects.get(id=id)
    return render(request, 'order_result.html', { 'order' : order })