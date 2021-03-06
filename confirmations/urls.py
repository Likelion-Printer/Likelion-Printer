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
import confirmations.views

urlpatterns = [
    path("my_order/", confirmations.views.my_order, name="my_order"),
    path("manage_order/", confirmations.views.manage_order, name="manage_order"),
    path("manage_stats/", confirmations.views.manage_stats, name="manage_stats"),
    path("complete/<int:id>", confirmations.views.complete, name="complete"),
    path("take_back/<int:id>", confirmations.views.take_back, name="take_back"),
]
