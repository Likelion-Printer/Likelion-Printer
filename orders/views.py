from django.shortcuts import render, redirect
from . models import *
from confirmations.models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def step1(request):
    if not(request.user.is_authenticated):
        return redirect('error_home')
    return render(request, 'step1.html')

def error_home(request):
    msg = 'error'
    return render(request, 'home.html', {'msg': msg})

def create_order(request):
    order = Order()
    order.customer = request.user
    order.options_print = request.POST.get('optionDirection')
    order.options_pages = request.POST.get('pagePerSheet')
    order.options_print = request.POST.get('optionPrint')
    order.options_color = request.POST.get('optionColor')
    order.options_flip = request.POST.get('optionFlip')
    order.number_of_pages = request.POST.get('numPages')
    order.comments = request.POST.get('request')
    order.cost()
    order.order_num()
    order.save()
    id = order.pk
    files = request.FILES.getlist('mutipleFiles')
    print(files)
    for file in files:
        file_obj = File()
        file_obj.order_file = file
        file_obj.order = Order.objects.get(id=id)
        file_obj.save()
    return redirect('step2' , id)

def step2(request, id):
    order = Order.objects.get(id=id)
    # 프린트 가게 order = Order(printer_house_id = 1)
    # 픽업 시간
    return render(request, 'step2.html', { 'order' : order })

def payment(request, id):
    order = Order.objects.get(id=id)
    return render(request, 'payment.html', { 'order' : order })

def order_result(request, id):
    order = Order.objects.get(id=id)
    return render(request, 'order_result.html', { 'order' : order })