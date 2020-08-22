#!/usr/bin/env python
# -*-coding:utf-8-*-
from django.urls import path
from . import views


urlpatterns = [
    path('call_add/', views.call_add),
    path('get_add_result/', views.get_add_result, name='get_add_result'),
]
