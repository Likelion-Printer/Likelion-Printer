from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import get_user_model
# import requests
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



def kakao_login(request):
    # REST_API_KEY = os.environ.get("K_KEY")
    REST_API_KEY = "0aa937d977a340d30be56ee87e9c2f67"
    REDIRECT_URI = "http://127.0.0.1:8000/accounts/login/kakao/callback"
    return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code")

class KakaoException(Exception):
    pass

def kakao_callback(request):
    try:
        code =request.GET.get("code")
        REST_API_KEY = "0aa937d977a340d30be56ee87e9c2f67"
        REDIRECT_URI = "http://127.0.0.1:8000/accounts/login/kakao/callback"
        token_request = requests.get(f"https://kauth.kakao.com?grant_type=authorization_code&client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&code={code}")
        token_json = token_request.json()
        error = token_json.get("error", None)
        if error is not None:
            raise KakaoException()
        
        access_token = token_json.get("access_token")
        profile_request = requests.get(
            "https://kapi.kakao.com/v1/user/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        profile_json = profile_request.json()
        email = profile_json.get("kaccount_email", None)
        if email is None:
            raise KakaoException()
        properties = profile_json.get("properties")
        nickname = properties.get("nickname")
        profile_image = properties.get("profile_image")
        try:
            user = models.User.objects.get(email=email)
            if user.login_method != models.User.LOGING_KAKAO:
                raise KakaoException(f"Please log in with: {user.login_method}")
        except models.User.DoesNotExist:
            user = models.User.objects.create(
                email=email,
                username=email,
                first_name=nickname,
                login_method=models.User.LOGING_KAKAO,
                email_verified=True,
            )
            user.set_unusable_password()
            user.save()
            if profile_image is not None:
                photo_request = requests.get(profile_image)
                user.avatar.save(
                    f"{nickname}-avatar", ContentFile(photo_request.content)
                )
        messages.success(request, f"Welcome back {user.first_name}")
        login(request, user)
        return redirect(reverse("home/"))
    except KakaoException as e:
        messaves.error(request, e)
        return redirect(reverse("login/"))