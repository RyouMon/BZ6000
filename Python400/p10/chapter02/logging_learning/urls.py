#!/usr/bin/env python
# -*-coding:utf-8-*-
from django.urls import path
from . import views


app_name = 'logging_learning'


urlpatterns = [
    path('', views.log, name='log'),
]