from django.shortcuts import render, redirect
from .models import *
from confirmations.models import *
from django.http import HttpResponse
import json
from django.core import serializers
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
#from PyPDF2 import PdfFileReader
from django.core.paginator import Paginator
# from PyPDF2 import PdfFileReader

# Create your views here.

User = get_user_model()


def home(request):
    return render(request, 'home.html')

def step1(request):
    if not(request.user.is_authenticated):
        return redirect('error_home')
    return render(request, 'step1.html')

    
def step3(request):
    return render(request, 'step3.html')

def error_home(request):
    msg = 'error'
    return render(request, 'home.html', {'msg': msg})

@csrf_exempt
def create_order(request):
    order = Order()
    order.customer = request.user
    print(request.user)
    order.options_print = request.POST.get('optionDirection')
    print(request.POST.get('optionDirection'))
    order.options_pages = request.POST.get('pagePerSheet')
    order.options_print = request.POST.get('optionPrint')
    order.options_color = request.POST.get('optionColor')
    order.options_flip = request.POST.get('optionFlip')
    order.number_of_pages = request.POST.get('numPages')
    print(order.number_of_pages)
    order.comments = request.POST.get('request')
    order.cost()
    order.order_num()
    order.save()
    id = order.pk
    file = request.FILES['file']
    file_obj = File()
    file_obj.name = file.name
    file_obj.size = file.size # 단위는 byte
    file_obj.order_file = file
    file_obj.order = Order.objects.get(id=id)
    file_obj.save()
    # <pdf 페이지 수 구하기>
    # pdf = PdfFileReader(open(file_obj.order_file.path,'rb'))
    # print(pdf.getNumPages())
    # word, hwp
    return redirect('step2' , id)

def step2(request, id):
    order = Order.objects.get(id=id)
    printer = Printer_house.objects.all()
    paginator = Paginator(printer, 3)
    page = request.GET.get('page')
    printerhouse = paginator.get_page(page)
    page_size= 3
    return render(request, 'step2.html', { 'order' : order, 'printerhouse' : printerhouse })

def update_order(request, id):
    order = Order.objects.get(id=id)
    printerhouse_id = request.POST.get('printerHouse')
    order.printer_house = Printer_house.objects.get(id=printerhouse_id)
    order.pickup_time = request.POST.get('pickupTime')
    order.is_in_process = False
    order.save()
    return redirect('payment', id)

def payment(request, id):
    order = Order.objects.get(id=id)
    return render(request, 'payment.html', { 'order' : order })

def order_result(request, id):
    order = Order.objects.get(id=id)
    return render(request, 'order_result.html', { 'order' : order })

# @user_passes_test(lambda u: u.is_staff)
def printerhouse_info(request, id):

    order = Order.objects.filter(printer_house_id = id, is_in_process = 'False', is_canceled = 'False').exclude(status = 'picked_up')
    order_list = serializers.serialize('json', order)
    response_data = {}

    try:
        response_data['result'] = 'Success'
        response_data['message'] = order_list

    except:
        response_data['result'] = 'Failed'
        response_data['message'] = 'Failed'

    return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def upload_file(request):
    file = request.FILES['file']
    file_obj = File()
    file_obj.name = file.name
    file_obj.size = file.size # 단위는 byte
    file_obj.order_file = file
    file_obj.order = Order.objects.get(id=id)
    file_obj.save()
    return render(request, 'home.html')

def step3(request,id):
    order = Order.objects.get(id=id)
    return render(request, 'step3.html', { 'order' : order })

