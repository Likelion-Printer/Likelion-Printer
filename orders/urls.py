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
import orders.views

urlpatterns = [
    path('step1/', orders.views.step1, name='step1'),
    path('create_order', orders.views.create_order, name='create_order'),
    path('step2/<int:id>', orders.views.step2, name='step2'),
    path('step3/<int:id>', orders.views.step3, name='step3'),
    path('update_order/<int:id>', orders.views.update_order, name='update_order'),
    path('payment/<int:id>', orders.views.payment, name='payment'),
    path('order_result/<int:id>', orders.views.order_result, name='order_result'),
    path('api/<int:id>', orders.views.printerhouse_info, name='printerhouse_info'),
    path('file_api/', orders.views.upload_file, name='upload_file'),
]
