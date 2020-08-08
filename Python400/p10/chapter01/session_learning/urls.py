#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from . import views


app_name = 'session_learning'


urlpatterns = [
    path('test/', views.test_session),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('index/', views.index, name='index'),
]
