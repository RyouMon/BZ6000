#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from . import views


app_name = 'middleware_learning'


urlpatterns = [
    path('', views.index, name='index'),
]
