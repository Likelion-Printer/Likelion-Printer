"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import accounts.views

urlpatterns = [
    path('login/', accounts.views.login, name='login'),
    path('signup/', accounts.views.signup, name='signup'),
    path('logout/', accounts.views.logout, name="logout"),
    path('staff_login/', accounts.views.staff_login, name='staff_login'),
    path('login/kakao', accounts.views.kakao_login, name= "kakao-login"),
    # path('login/kakao/callback', accounts.views.kakao_callback, name= "kakao-callback"),
    path('test/', accounts.views.test, name= "test"),
]
