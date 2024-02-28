# -*- coding: utf-8 -*-

"""
@author: Aaron.An
@contact: QQ:294964314
@Created on: 2024/2/25 23:05
@Remark: 
"""
from django.urls import path

from users import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),

]
