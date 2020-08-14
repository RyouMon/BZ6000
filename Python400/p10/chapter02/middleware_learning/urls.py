#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from . import views


app_name = 'middleware_learning'


urlpatterns = [
    path('', views.index, name='index'),
    path('template_response/', views.test_process_template_response, name='test_process_template_response'),
]
