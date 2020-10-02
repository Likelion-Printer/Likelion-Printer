from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': '아이디나 비밀번호가 일치하지 않습니다. 다시 입력해주세요.'})

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username = request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('login')
        else:
            return render(request, 'signup.html', {'error': '잘못 입력된 항목이 있습니다.'})
            
    return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def staff_login(request):
    return render(request, 'staff_login.html')