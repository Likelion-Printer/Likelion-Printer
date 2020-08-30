from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def print_setting(request):
    return render(request, 'print_setting.html')