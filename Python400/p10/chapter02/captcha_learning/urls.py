#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from . import views


app_name = 'captcha_learning'


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('captcha/', views.captcha_img, name='captcha_img'),
]
