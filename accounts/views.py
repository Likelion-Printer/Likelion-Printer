from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def staff_login(request):
    return render(request, 'staff_login.html')